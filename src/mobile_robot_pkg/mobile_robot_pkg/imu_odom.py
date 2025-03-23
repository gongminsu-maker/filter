import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
import math
import numpy as np
import os
import pandas as pd

class ImuOdometry(Node):
    def __init__(self):
        super().__init__('imu_odometry')
        
        # 초기 상태 변수
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.omega = 0.0
        self.last_time = self.get_clock().now()
        
        # Odometry 메시지 발행
        self.odom_pub = self.create_publisher(Odometry, '/odom_imu', 10)
        
        # IMU 메시지 구독
        self.create_subscription(Imu, '/imu/data', self.imu_callback, 10)

        # 저장공간
        self.log_data = []
    
    def imu_callback(self, msg):
    # 현재 시간 가져오기
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9  # 초 단위 변환
        self.last_time = current_time

        if dt == 0:
            return

    # IMU 센서 값 가져오기
        accel_x = msg.linear_acceleration.x
        accel_y = msg.linear_acceleration.y
        x = round(msg.orientation.x,6)
        y = round(msg.orientation.y,6)
        z = round(msg.orientation.z,6)
        w = round(msg.orientation.w,6)
        q = self.quaternion_to_yaw(x,y,z,w)
        self.log_data.append(q) # rad/s단위

    # 속도 업데이트 (가속도를 적분)
        self.vx += accel_x * dt
        self.vy += accel_y * dt

    # 위치 업데이트 (속도를 적분)
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.theta = q
        self.get_logger().info(f"theta{self.theta*57.295779513082320876798154814105}°")




    # Odometry 메시지 생성
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_link'
        odom_msg.pose.pose.position.x = self.x
        odom_msg.pose.pose.position.y = self.y
        odom_msg.pose.pose.position.z = self.theta

    # Twist 정보 업데이트 (선속도 및 각속도)
        odom_msg.twist.twist.linear.x = self.vx
        odom_msg.twist.twist.linear.y = self.vy

    # 메시지 발행
        self.odom_pub.publish(odom_msg)


    def save_to_excel(self):
        df = pd.DataFrame(self.log_data, columns=["z"])
        file_path = os.path.join(os.getcwd(), "sensor_fusion_log.xlsx")
        df.to_excel(file_path, index=False, engine='openpyxl')
        print(f"[📂] 데이터 저장 완료: {file_path}")
    def quaternion_to_yaw(self,x,y,z,w):
        yaw = -math.atan2(2*(x*y-w*z),2*(w*w+x*x)-1)
        return yaw


def main(args=None):
    rclpy.init(args=args)
    node = ImuOdometry()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.save_to_excel()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
