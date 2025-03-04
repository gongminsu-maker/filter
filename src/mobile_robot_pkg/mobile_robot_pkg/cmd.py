import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class CmdVelController(Node):
    def __init__(self):
        super().__init__('cmd_vel_controller')

        # ROS2 퍼블리셔 설정
        self.cmd_vel_publisher = self.create_publisher(Twist, '/cmd_vel', 10)

    def send_velocity_commands(self):
        """ 순차적인 속도 명령 실행 """
        input("Press Enter to start motion...")

        twist_msg = Twist()

        # 1️⃣ 직진 (4초)
        twist_msg.linear.x = 0.17
        twist_msg.angular.z = 0.0
        self.cmd_vel_publisher.publish(twist_msg)
        self.get_logger().info("Moving straight for 4 seconds...")
        time.sleep(4)

        # 2️⃣ 회전 (4초)
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 2.0
        self.cmd_vel_publisher.publish(twist_msg)
        self.get_logger().info("Rotating for 4 seconds...")
        time.sleep(3)

        # 3️⃣ 직진 + 회전 동시 수행 (4초)
        #twist_msg.linear.x = 0.12
        #twist_msg.angular.z = 2.0
        #self.cmd_vel_publisher.publish(twist_msg)
        #self.get_logger().info("Moving straight and rotating for 4 seconds...")
        #time.sleep(2)

        # 4️⃣ 정지
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.0
        self.cmd_vel_publisher.publish(twist_msg)
        self.get_logger().info("Stopping.")

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelController()
    node.send_velocity_commands()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
