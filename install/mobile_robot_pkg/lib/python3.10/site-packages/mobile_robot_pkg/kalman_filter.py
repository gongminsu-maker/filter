import rclpy
import math
import numpy as np
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Pose, Quaternion
import pandas as pd
import os

class EKFNode(Node):
    def __init__(self):
        super().__init__('ekf_node')

        self.update_rate = 10  # Hz
        self.dt = 1.0 / self.update_rate  # 주기
       
        # 엔코더 속도 초기값
        self.v_enc = 0.0
        self.w_enc = 0.0
        
        # IMU 초기값
        self.yaw_imu = 0.0
        self.a_x = 0.0
        self.a_y = 0.0

        # EKF 상태 벡터 [x, y, theta]
        self.x = np.zeros((3, 1))
        self.z = np.zeros((3,1))

        # 상태 공분산 행렬 P (초기값)
        self.P = np.eye(3)

        # 프로세스 노이즈 행렬 Q
        self.Q = np.diag([2.0, 2.0, 0.05])

        # 측정 모델 행렬 H
        self.H = np.eye(3)  # 단순 위치 및 각도 측정 반영

        # 측정 노이즈 행렬 R
        self.R = np.diag([0.00025, 0.005, 0.001])  # x, y, yaw 측정 노이즈

        # 최신 센서 데이터 저장용 변수
        self.latest_odom = None
        self.latest_imu = None
        self.log_data = []

        # ROS 2 토픽 구독
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.imu_sub = self.create_subscription(Imu, '/imu/data', self.imu_callback, 10)

        # 보정된 Pose 데이터 발행
        self.pose_pub = self.create_publisher(Pose, '/pose_corrected', 10)

        self.timer = self.create_timer(self.dt, self.ekf_prediction)

    def quaternion_to_yaw(self, x, y, z, w):
        """ 쿼터니언을 Yaw 값(라디안)으로 변환 """
        return -math.atan2(2 * (-y) * x - 2 * w * z, 2 * w * w + 2 * x * x - 1)

    def yaw_to_quaternion(self, yaw):
        """ Yaw 값을 쿼터니언으로 변환 """
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        return Quaternion(x=0.0, y=0.0, z=sy, w=cy)
    def normalize_angle(self, angle):
        while angle > np.pi:  # 180° 초과 시 -360° 보정
            angle -= 2.0 * np.pi
        while angle < -np.pi:  # -180° 미만 시 +360° 보정
            angle += 2.0 * np.pi
        return angle


    def odom_callback(self, msg):
        """ 엔코더 데이터를 수신하고 선속도 및 각속도를 저장 """
        self.latest_odom = msg
        self.v_enc = msg.twist.twist.linear.x
        self.w_enc = msg.twist.twist.angular.z

    def imu_callback(self, msg):
        """ IMU 데이터를 수신하고 Yaw 및 가속도 저장 """
        self.latest_imu = msg
        self.a_x = msg.linear_acceleration.x
        if 0.0 < self.a_x < 0.02:
            self.a_x = 0.0
        
        self.a_y = msg.linear_acceleration.y
        q = msg.orientation
        self.yaw_imu = self.quaternion_to_yaw(q.x, q.y, q.z, q.w)
        #self.get_logger().info(f"Raw Yaw (from IMU): {self.yaw_imu}°")
        #self.get_logger().info(f"ax= {self.a_x}")

    def ekf_prediction(self):
        """ EKF 예측 단계 """
        if self.latest_odom is None or self.latest_imu is None:
            return  # 센서 데이터가 아직 없음

        theta = self.x[2, 0]  # 현재 Yaw (rad)
        delta_s = self.v_enc * self.dt  # 엔코더 기반 이동 거리
        self.delta_theta = self.w_enc * self.dt  # 엔코더 기반 각속도 적분
        
        # 상태 전이 행렬 F_k
        F_k = np.array([
            [1, 0, -delta_s * math.sin(theta + self.delta_theta / 2)],
            [0, 1,  delta_s * math.cos(theta + self.delta_theta / 2)],
            [0, 0, 1]
        ])
        
        # 입력 행렬 B_k
        B_k = np.array([
            [math.cos(theta + self.delta_theta / 2), -0.5 * delta_s * math.sin(theta + self.delta_theta / 2)],
            [math.sin(theta + self.delta_theta / 2),  0.5 * delta_s * math.cos(theta + self.delta_theta / 2)],
            [0, 1]
        ])

        # 입력 벡터 u_k
        u_k = np.array([[delta_s], [self.delta_theta]])

        # 상태 예측: x_k = F_k * x_k-1 + B_k * u_k
        self.x = F_k @ self.x + B_k @ u_k

        # 공분산 예측: P_k = F_k * P_k-1 * F_k.T + Q
        self.P = F_k @ self.P @ F_k.T + self.Q

        self.ekf_update()

    def ekf_update(self):
        """ EKF 보정 단계 """
        Z = np.array([
            [self.z[0, 0] + self.v_enc * math.cos(self.delta_theta) * self.dt],#+0.5 * self.a_x * self.dt ** 2],
            [self.z[1, 0] + self.v_enc * math.sin(self.delta_theta) * self.dt],#+ 0.5 * self.a_y * self.dt ** 2],
            [self.yaw_imu]
        ])
        self.z[0,0] += self.v_enc * math.cos(self.delta_theta) * self.dt
        self.z[1, 0] += self.v_enc * math.sin(self.delta_theta) * self.dt

         # EKF 업데이트 전 상태 로그
        #self.get_logger().info(f"[EKF Before] x={self.x[0,0]:.4f}, y={self.x[1,0]:.4f}, yaw={math.degrees(self.x[2,0]):.2f}°")
        #self.get_logger().info(f"[EKF Before] yaw_imu (Raw IMU) = {math.degrees(self.yaw_imu):.2f}°")
        # 칼만 이득 K 계산
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)

        # 상태 업데이트
        self.x = self.x + K @ (Z - (self.H @ self.x))

        # 공분산 업데이트
        self.P = (np.eye(3) - K @ self.H) @ self.P
        #  Yaw 값 정규화 적용 (튀는 값 방지)
        self.x[2, 0] = self.normalize_angle(self.x[2, 0])
        #self.get_logger().info(f"[EKF After] x={self.x[0,0]:.4f}, y={self.x[1,0]:.4f}, yaw={math.degrees(self.x[2,0]):.2f}°")

        self.publish_corrected_pose()
    #     self.log_data.append([K])
    #     self.save_to_excel()


    # def save_to_excel(self):
    #     df = pd.DataFrame(self.log_data, columns=['K'])
    #     file_path = os.path.join(os.getcwd(), "sensor_fusion_log.xlsx")
    #     df.to_excel(file_path, index=False, engine='openpyxl')
    #     print(f"[📂] 데이터 저장 완료: {file_path}")

    def publish_corrected_pose(self):
        """ 보정된 Pose 데이터를 발행 """
        pose_msg = Pose()
        pose_msg.position.x = float(self.x[0, 0])
        pose_msg.position.y = float(self.x[1, 0])
        pose_msg.orientation = self.yaw_to_quaternion(float(self.x[2, 0]))

        self.pose_pub.publish(pose_msg)
        self.get_logger().info(f"x {pose_msg.position.x} y {pose_msg.position.y} yaw {float(self.x[2,0])*57.295779513082320876798154814105}")

def main(args=None):
    rclpy.init(args=args)
    node = EKFNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
