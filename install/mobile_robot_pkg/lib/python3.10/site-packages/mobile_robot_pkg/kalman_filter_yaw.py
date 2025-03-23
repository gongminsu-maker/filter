import rclpy
import math
import numpy as np
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Pose, Quaternion
from my_custom_message.msg import Visual
from geometry_msgs.msg import PoseStamped
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
        self.Q = np.diag([1.0, 1.0, 0.05])

        # 측정 모델 행렬 H
        self.H = np.array([[0,0,1]])  # 단순 위치 및 각도 측정 반영

        # 측정 노이즈 행렬 R
        self.R = np.array([2.7*1e-3])  
        # yaw(radian) 측정 노이즈 짧은 테스트 => drift오차 무시
        # x,y는 측정 데이터 부재로 신뢰하지 않게 만듦. 이후 라이다 센서로 대체

        # 최신 센서 데이터 저장용 변수
        self.latest_odom = None
        self.latest_imu = None
        self.log_data = []

        # ROS 2 토픽 구독
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.imu_sub = self.create_subscription(Imu, '/imu/data', self.imu_callback, 10)

        # 보정된 Pose 데이터 발행
        self.pose_pub = self.create_publisher(Pose, '/pose_corrected', 10)
        # 시각화 토픽 발행
        self.visual_pub = self.create_publisher(Visual,'/visual',10)
        # rviz 토픽 발행
        self.predict = self.create_publisher(PoseStamped,'/predict',10)
        self.sensor = self.create_publisher(PoseStamped,'/sensor',10)
        self.filter = self.create_publisher(PoseStamped,"/filter",10)

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
        self.ori = msg.pose.pose.orientation
        self.theta = self.quaternion_to_yaw(self.ori.x, self.ori.y, self.ori.z, self.ori.w)

    def imu_callback(self, msg):
        """ IMU 데이터를 수신하고 Yaw 및 가속도 저장 """
        self.latest_imu = msg
        self.a_x = msg.linear_acceleration.x
        if 0.0 < self.a_x < 0.02:
            self.a_x = 0.0
        
        self.a_y = msg.linear_acceleration.y
        self.q = msg.orientation
        self.yaw_imu = self.quaternion_to_yaw(self.q.x, self.q.y, self.q.z, self.q.w)
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

        # 상태 예측: x_k = f(xk-1 , uk)
        self.x[0,0] += delta_s*math.cos(theta + self.delta_theta/2)
        self.x[1,0] += + delta_s*math.sin(theta + self.delta_theta/2)
        self.x[2,0]= theta + self.delta_theta


        # 공분산 예측: P_k = F_k * P_k-1 * F_k.T + Q
        self.P = F_k @ self.P @ F_k.T + self.Q
        # 상태예측 log
        self.get_logger().info(f"[EKF before] x={self.x[0,0]}, y={self.x[1,0]}, yaw={float(self.x[2,0])*57.295779513082320876798154814105}°")


        self.ekf_update()

    def ekf_update(self):
        """ EKF 보정 단계 """
        Z = np.array([[self.yaw_imu]])

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
        self.visual()
        self.rviz()
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
        self.get_logger().info(f"after ekf: x {pose_msg.position.x} y {pose_msg.position.y} yaw {float(self.x[2,0])*57.295779513082320876798154814105}")
    
    def visual(self):
        plot = Visual()
        plot.yaw_filter = self.x[2,0]*57.295779513082320876798154814105
        plot.yaw_odom = self.theta*57.295779513082320876798154814105
        plot.yaw_imu = self.yaw_imu*57.295779513082320876798154814105
        self.visual_pub.publish(plot)

    def rviz(self):
        now = self.get_clock().now().to_msg()
        pos_predict = PoseStamped()
        pos_estimate = PoseStamped()
        pos_filter= PoseStamped()

        pos_predict.header.stamp = now
        pos_predict.header.frame_id = 'odom'
        pos_predict.pose.orientation = self.ori # 
        self.predict.publish(pos_predict)
        pos_estimate.header.stamp = now
        pos_estimate.header.frame_id = 'odom'
        pos_estimate.pose.orientation = self.q 
        self.sensor.publish(pos_estimate)
        pos_filter.header.stamp = now
        pos_filter.header.frame_id = 'odom'
        pos_filter.pose.orientation = self.yaw_to_quaternion(float(self.x[2, 0])) 
        self.filter.publish(pos_filter)

def main(args=None):
    rclpy.init(args=args)
    node = EKFNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
