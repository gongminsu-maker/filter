import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import math
import time

class Square(Node):
    def __init__(self):
        super().__init__("square_node")
        self.current_x = None
        self.current_y = None
        self.current_theta = None

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.sub = self.create_subscription(Odometry, "/odom", self.sub_callback, 10)
        self.get_logger().info("🛰️ sub 성공")

        # 🔥 목표 설정
        self.targets = [
            ("x", 1.0),
            ("theta", 90),
            ("y", 0.6),
            ("theta", 180),
            ("x", 0.0),
            ("theta", -90),
            ("y", 0.0)
        ]

        self.stage = 0
        self.twist = Twist()
        self.timer = self.create_timer(0.1, self.control_loop)  # 🔥 0.1초마다 실행

        # ✅ **속도 설정**
        self.max_speed = 0.08  # 🔥 이동 속도 0.08 m/s
        self.max_turn_speed = 0.5  # 🔥 회전 속도 0.5 rad/s

    def quaternion_to_yaw(self, quaternion):
        """ 사원수를 Yaw 각도로 변환 """
        x, y, z, w = quaternion.x, quaternion.y, quaternion.z, quaternion.w
        yaw = math.atan2(2 * (w * z + x * y), 1 - 2 * (y ** 2 + z ** 2))
        return math.degrees(yaw)

    def sub_callback(self, msg):
        """ 오도메트리 콜백 - 현재 위치 업데이트 """
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        self.current_theta = self.quaternion_to_yaw(msg.pose.pose.orientation)

    def control_loop(self):
        """ 주기적으로 위치를 확인하고 목표 도달 여부 체크 """
        if self.stage >= len(self.targets):
            self.get_logger().info("✅ 4각형 주행 완료!")
            return
        
        move_type, target_value = self.targets[self.stage]

        if move_type == "x":
            self.move_forward_x(target_value)
        elif move_type == "y":
            self.move_forward_y(target_value)
        elif move_type == "theta":
            self.turn(target_value)

    def move_forward_x(self, target_x):
        """ 목표 x 위치까지 직진 """
        if self.current_x is None:
            return
        
        remaining_distance = abs(target_x - self.current_x)
        if remaining_distance <= 0.05:
            self.get_logger().info("🛑 목표 x 도달! 정지")
            self.stop_and_wait()
            return

        self.twist.linear.x = self.max_speed  # ✅ **속도를 0.08 m/s로 유지**
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)

    def move_forward_y(self, target_y):
        """ 목표 y 위치까지 직진 """
        if self.current_y is None:
            return

        remaining_distance = abs(target_y - self.current_y)
        if remaining_distance <= 0.05:
            self.get_logger().info("🛑 목표 y 도달! 정지")
            self.stop_and_wait()
            return

        self.twist.linear.x = self.max_speed  # ✅ **속도를 0.08 m/s로 유지**
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)

    def turn(self, target_theta):
        """ 목표 각도까지 회전 """
        if self.current_theta is None:
            return

        angle_diff = (target_theta - self.current_theta + 180) % 360 - 180  
        remaining_angle = abs(angle_diff)

        if remaining_angle <= 3.0:
            self.get_logger().info("🛑 목표 각도 도달! 정지")
            self.stop_and_wait()
            return

        self.twist.linear.x = 0.0
        self.twist.angular.z = math.copysign(self.max_turn_speed, angle_diff)  # ✅ **속도를 0.5 rad/s로 유지**
        self.pub.publish(self.twist)

    def stop_and_wait(self):
        """ 현재 동작을 멈추고 2초 대기 후 다음 단계로 이동 """
        self.get_logger().info("🛑 정지 후 2초 대기")
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)
        time.sleep(2)

        self.stage += 1  # 다음 목표로 이동

def main(args=None):
    rclpy.init(args=args)
    node = Square()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
