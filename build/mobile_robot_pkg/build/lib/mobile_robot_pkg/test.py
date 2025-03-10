import rclpy
import numpy as np
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist, Pose

class StopAtX(Node):
    def __init__(self):
        super().__init__('stop_at_x')
        self.last_time = self.get_clock().now().to_msg().sec
        self.position = [0.0, 0.0, 0.0]  # [x, y, theta]
        self.velocity = [0.0, 0.0, 0.0]  # [vx, vy, omega]
        self.acceleration= [0.0, 0.0]
        self.angular_vel = 0.0

        # fixed threshold 설정
        self.threshold = 0.0
        # dynamic threshold 설정
        self.thres_data = []

        #self.use_ekf = use_ekf  # True이면 EKF 기반, False이면 오도메트리 기반
        self.target_x = 0.7  # 목표 거리
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.imu_sub = self.create_subscription(Imu,'/imu/data',self.imu_callback, 10)
        self.subscription = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.get_logger().info("Using Odometry-based stopping.")

        # 초기 이동 명령 발행
        self.send_velocity_command()

    def imu_callback(self, msg):

        self.acceleration = [msg.linear_acceleration.x, msg.linear_acceleration.y]
        self.angular_vel = msg.angular_velocity.z
        self.thres_data.append(np.sqrt(self.acceleration[0]**2 + self.acceleration[1] **2))
        self.update()

    def send_velocity_command(self):
        input("Press Enter to start motion...")
        """ 속도 명령을 발행하는 함수 """
        self.twist = Twist()
        self.twist.linear.x = 0.15
        self.cmd_vel_pub.publish(self.twist)

    def odom_callback(self, msg):
        """ 오도메트리 기반 정지 """
        current_x = msg.pose.pose.position.x
        #self.get_logger().info(f"Odom X: {current_x:.3f}")

        if current_x >= self.target_x:
            self.twist.linear.x = 0.0
            self.cmd_vel_pub.publish(self.twist)
            self.get_logger().info(f"Stopping! Reached {self.target_x}m")

    def pose_callback(self, msg):
        """ EKF 기반 정지 """
        current_x = msg.position.x
        self.get_logger().info(f"EKF X: {current_x:.3f}")

        if current_x >= self.target_x:
            self.twist.linear.x = 0.0
            self.cmd_vel_pub.publish(self.twist)
            self.get_logger().info(f"Stopping! Reached {self.target_x}m")

    def update(self):
        current_time = self.get_clock().now().to_msg().sec
        dt = current_time - self.last_time
        self.last_time = current_time

        # dynamic threshold
        if np.abs(self.twist.linear.x) == 0.0:
            num = 20        
            if len(self.thres_data) >= num:
                self.threshold = np.max(self.thres_data[-num:])
                print(f"new_threshold: {self.threshold}")  

        # static threshold
        below_threshold = np.sqrt(self.acceleration[0]**2 + self.acceleration[1] **2)
        if below_threshold <= self.threshold:
            self.velocity[:2] = [0.0, 0.0]
        else:
            self.velocity[0] = self.acceleration[0]* dt
            self.velocity[1] = self.acceleration[1] * dt
            self.position[0] += self.velocity[0] * dt + 0.5* self.acceleration[0] * dt**2
            self.position[1] += self.velocity[1] * dt + 0.5* self.acceleration[1] * dt**2
            

        self.position[2] += self.angular_vel

        # self.velocity[0] += self.acceleration[0] * dt
        # self.velocity[1] += self.acceleration[1] * dt
        # self.velocity[2] = self.angular_vel

        pub_msg = Imu()
        pub_msg.linear_acceleration.x = self.acceleration[0]
        pub_msg.linear_acceleration.y = self.acceleration[1]
        pub_msg.angular_velocity.z = self.velocity[2]
        self.get_logger().info(f'pos_x: {self.position[0]}')
        self.get_logger().info(f'pos_y: {self.position[1]}')
        self.get_logger().info(f'pos_th: {self.position[2]}')

        #self.imu_corrected_pub.publish(pub_msg)

def main(args=None):
    rclpy.init(args=args)

    # 오도메트리 기반 정지 노드 실행
    node = StopAtX()  # 오도메트리 기준 정지
    #node = StopAtX(use_ekf=True)  # EKF 기준 정지


    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
