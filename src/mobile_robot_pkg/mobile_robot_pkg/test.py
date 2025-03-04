import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Pose

class StopAtX(Node):
    def __init__(self, use_ekf=True):
        super().__init__('stop_at_x')

        self.use_ekf = use_ekf  # True이면 EKF 기반, False이면 오도메트리 기반
        self.target_x = 0.7  # 목표 거리
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # 구독할 토픽 선택
        if self.use_ekf:
            self.subscription = self.create_subscription(Pose, '/pose_corrected', self.pose_callback, 10)
            self.get_logger().info("Using EKF-based stopping.")
        else:
            self.subscription = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
            self.get_logger().info("Using Odometry-based stopping.")

        # 초기 이동 명령 발행
        self.send_velocity_command()

    def send_velocity_command(self):
        input("Press Enter to start motion...")
        """ 속도 명령을 발행하는 함수 """
        self.twist = Twist()
        self.twist.linear.x = 0.17
        self.cmd_vel_pub.publish(self.twist)

    def odom_callback(self, msg):
        """ 오도메트리 기반 정지 """
        current_x = msg.pose.pose.position.x
        self.get_logger().info(f"Odom X: {current_x:.3f}")

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

def main(args=None):
    rclpy.init(args=args)

    # 오도메트리 기반 정지 노드 실행
    # node = StopAtX(use_ekf=False)  # 오도메트리 기준 정지
    node = StopAtX(use_ekf=True)  # EKF 기준 정지

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
