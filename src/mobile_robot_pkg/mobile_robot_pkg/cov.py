import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from scipy.spatial.transform import Rotation as R
import numpy as np
import time

class RtCalculator(Node):
    def __init__(self):
        super().__init__('rt_calculator')

        # ROS2 구독 설정 (cmd_vel과 odom 구독)
        self.odom_subscription = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.cmd_vel_subscription = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

        # 데이터 수신 확인 플래그
        self.received_cmd_vel = False
        self.received_odom = False
        self.start_time = None  # 데이터 수집 시작 시간
        self.last_time = None

        # 목표 위치 (초기값을 None으로 설정)
        self.target_x = None
        self.target_y = None
        self.target_theta = None

        self.linear_v = None
        self.angular_v = None

        # 오차 데이터 저장 리스트
        self.errors = []
        self.max_samples = 50  # 최대 30개 데이터 수집 후 종료
        self.sample_count = 0

    def compute_Rt(self):
        errors_array = np.array(self.errors).T  # (6,30) 형태 변환
        Rt = np.cov(errors_array)  # 공분산 행렬 계산 (6×6)
        print("\nComputed R_t (Covariance Matrix):")
        print("-" * 50)
        np.set_printoptions(precision=6, suppress=True)
        formatted_Rt = np.array2string(Rt, separator=",")
        print(formatted_Rt)
        print("-" * 50)
        print("\nRt Calculation Completed. Node will shut down.")

    def cmd_vel_callback(self, msg):
        if not self.received_cmd_vel:
            self.received_cmd_vel = True
            print("First cmd_vel received! Waiting for odometry sync...")
        self.linear_v = msg.linear.x
        self.angular_v = msg.angular.z
        if self.received_cmd_vel and self.received_odom and self.start_time is None:
            self.start_time = time.time()
            print("\nBoth cmd_vel & odom received! Starting data collection...\n")
    def quaternion_to_euler(self, quat):
        r = R.from_quat([quat.x, quat.y, quat.z, quat.w])  # Scipy를 이용한 변환
        _, _, yaw = r.as_euler('xyz', degrees=False)  # 라디안 단위로 변환
        return yaw  # yaw (theta) 값만 반환


    def odom_callback(self, msg):
        if not self.received_odom:
            self.received_odom = True
            print("✅ First odometry data received! Waiting for cmd_vel sync...")
        if self.received_cmd_vel and self.received_odom and self.start_time is None:
            self.start_time = time.time()
            self.last_time = self.start_time  # 초기 타임스탬프 설정
            print("\nBoth cmd_vel & odom received! Starting data collection...\n")
            self.target_x = msg.pose.pose.position.x
            self.target_y = msg.pose.pose.position.y
            self.target_theta = self.quaternion_to_euler(msg.pose.pose.orientation)

        if self.sample_count >= self.max_samples or self.start_time is None:
            return  
        
        if self.last_time is None:
            self.last_time = time.time()

        # ✅ 샘플 간 변화량을 반영한 dt 계산
        current_time = time.time()
        dt = current_time - self.last_time
        self.last_time = current_time  # 시간 업데이트
        if self.linear_v is None:
            self.linear_v = 0.0
        if self.angular_v is None:
            self.angular_v = 0.0
        if self.target_theta is None:
            self.target_theta = 0.0
        if self.target_x is None:
            self.target_x = 0.0
        if self.target_y is None:
            self.target_y = 0.0
        

    # ✅ 목표 위치 업데이트 (누적되지 않도록 dt만 반영)
        self.target_x += self.linear_v * np.cos(self.target_theta) * dt
        self.target_y += self.linear_v * np.sin(self.target_theta) * dt
        self.target_theta = (self.target_theta + self.angular_v * dt) % (2 * np.pi)

        measured_x = msg.pose.pose.position.x
        measured_y = msg.pose.pose.position.y
        measured_theta = self.quaternion_to_euler(msg.pose.pose.orientation)
        measured_vx = msg.twist.twist.linear.x
        measured_vy = msg.twist.twist.linear.y
        measured_vtheta = msg.twist.twist.angular.z

    # 📊 **오차 계산 (각도를 -π ~ π 범위로 정규화)**
        err_x = self.target_x - measured_x
        err_y = self.target_y - measured_y
        err_theta = (self.target_theta - measured_theta + np.pi) % (2 * np.pi) - np.pi
        err_vx = self.linear_v - measured_vx
        err_vy = 0 - measured_vy
        err_vtheta = self.angular_v - measured_vtheta

        self.errors.append([err_x, err_y, err_theta, err_vx, err_vy, err_vtheta])
        self.sample_count += 1

        print(f"\nIteration {self.sample_count}/{self.max_samples}")
        print("-" * 50)
        print(f"Target Position:   (x={self.target_x:.4f}, y={self.target_y:.4f}, θ={self.target_theta:.4f})")
        print(f"Actual Position:   (x={measured_x:.4f}, y={measured_y:.4f}, θ={measured_theta:.4f})")
        print(f"Position Error:    (dx={err_x:.4f}, dy={err_y:.4f}, dθ={err_theta:.4f})")
        print(f"⚡ Target Velocity:   (vx={self.linear_v:.4f}, vy=0, vθ={self.angular_v:.4f})")
        print(f" Actual Velocity:   (vx={measured_vx:.4f}, vy={measured_vy:.4f}, vθ={measured_vtheta:.4f})")
        print(f" Velocity Error:    (dvx={err_vx:.4f}, dvy={err_vy:.4f}, dvθ={err_vtheta:.4f})")
        print("-" * 50)
    
        if self.sample_count == self.max_samples:
            print("\n✅ 30 samples collected. Computing R_t...")
            self.compute_Rt()
            self.destroy_node()
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = RtCalculator()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
