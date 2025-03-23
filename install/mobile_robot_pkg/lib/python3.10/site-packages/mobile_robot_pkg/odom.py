import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
from my_custom_message.msg import Motor
import math
import numpy as np
import pandas as pd
import os
class DiffDriveOdometry(Node):
    def __init__(self):
        super().__init__('diff_drive_odometry')
        self.log_data = []
        
        # 로봇 파라미터
        self.wheel_diameter = 0.0875  # 87.5mm -> m 단위 변환
        self.wheel_base = 0.261       # 261mm -> m 단위 변환
        
        # 초기 상태 변수
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_time = self.get_clock().now()
        
        # Odometry 메시지 발행
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
        
        # Motor 메시지 구독
        self.create_subscription(Motor, '/motor_topic', self.motor_callback, 10)
        
        self.left_wheel_velocity = 0.0
        self.right_wheel_velocity = 0.0
        # left_wheel 정지상태 노이즈 필터링(0.044rad/s는 0.0018m/s임으로 무시가능한 수준.)
    def filter_wheel_noise(self,left_w, threshold=0.044):
        return 0.0 if abs(left_w) < threshold else left_w
        
    def motor_callback(self, msg):
        self.left_wheel_velocity = self.filter_wheel_noise(msg.left_w)
        self.right_wheel_velocity = msg.right_w
        #self.get_logger().info(f"left_w: {self.left_wheel_velocity}, right_w:{self.right_wheel_velocity}")
        self.update_odometry()

    def quaternion_from_euler(self,ai, aj, ak):
        ai /= 2.0  
        aj /= 2.0
        ak /= 2.0
        ci = math.cos(ai)  
        si = math.sin(ai)
        cj = math.cos(aj)
        sj = math.sin(aj)
        ck = math.cos(ak)
        sk = math.sin(ak)
        cc = ci*ck   
        cs = ci*sk
        sc = si*ck
        ss = si*sk

        q = np.empty((4, )) 
        q[0] = cj*sc - sj*cs  
        q[1] = cj*ss + sj*cc
        q[2] = cj*cs - sj*sc
        q[3] = cj*cc + sj*ss

        return q  
    def normalize_angle(self, angle):
    # θ=(θ+π)mod2π−π 정규화 공식.
        return (angle + math.pi) % (2 * math.pi) - math.pi
    
    def update_odometry(self):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9  # 초 단위 변환
        self.last_time = current_time
        
        # 바퀴 이동 거리 계산
        left_distance = self.left_wheel_velocity * (self.wheel_diameter / 2.0) * dt
        right_distance = self.right_wheel_velocity * (self.wheel_diameter / 2.0) * dt
        left_linear_v = self.left_wheel_velocity * (self.wheel_diameter / 2.0)
        right_linear_v = self.right_wheel_velocity * (self.wheel_diameter / 2.0)
        linear_v = (left_linear_v+right_linear_v)/2
        angular_v = (right_linear_v-left_linear_v)/(self.wheel_base /2.0)
        
        # 평균 이동 거리 및 회전각 계산
        delta_d = (left_distance + right_distance) / 2.0
        delta_theta = (right_distance - left_distance) / self.wheel_base
        
        # 위치 업데이트
        self.x += delta_d * math.cos(self.theta + delta_theta / 2.0)
        self.y += delta_d * math.sin(self.theta + delta_theta / 2.0)
        self.theta += delta_theta
           # Yaw 값 범위 조정 ([-π, π])
        self.theta = self.normalize_angle(self.theta)
        self.log_data.append([current_time.nanoseconds/1e9,self.theta*57.295779513082320876798154814105])
        
        
        # Quaternion 변환
        q = self.quaternion_from_euler(0,0,self.theta)
        
        # Odometry 메시지 생성
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_link'
        odom_msg.pose.pose.position.x = self.x
        odom_msg.pose.pose.position.y = self.y
        odom_msg.pose.pose.position.z = self.theta
        odom_msg.pose.pose.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
        
        # Twist 정보 업데이트 (선속도 및 각속도)
        odom_msg.twist.twist.linear.x = linear_v
        odom_msg.twist.twist.angular.z = angular_v
        
        # 메시지 발행
        self.odom_pub.publish(odom_msg)
        
        self.get_logger().info(f"Odometry Updated: x={self.x:.3f}, y={self.y:.3f}, theta={math.degrees(self.theta):.1f}°")
    def save_to_excel(self):
        df = pd.DataFrame(self.log_data, columns=["time","yaw"])
        file_path = os.path.join(os.getcwd(), "odom_theta.xlsx")
        df.to_excel(file_path, index=False, engine='openpyxl')
        print(f"[📂] 데이터 저장 완료: {file_path}")


def main(args=None):
    rclpy.init(args=args)
    node = DiffDriveOdometry()
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
