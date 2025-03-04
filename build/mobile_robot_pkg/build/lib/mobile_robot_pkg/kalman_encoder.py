import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from my_custom_message.msg import Motor
import numpy as np

class EKF(Node):
    def __init__(self):
        super().__init__('ekf_node')
        self.dt = 0.1 # 10HZ
        # 단위 [m]
        self.L = 0.261
        self.D = 0.0875

        # 상태 벡터 및 공분산 초기화
        self.state = np.zeros(6)
        self.P = np.eye(6) * 0.1

        # 노이즈 공분산 행렬
        self.Q = np.diag([0.1, 0.1, 0.01, 0.1, 0.1, 0.01])
        self.R = np.diag([0.05, 0.05, 0.01])

        # 퍼블리셔 및 서브스크라이버
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel_corrected', 10)
        self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        self.create_subscription(Motor, '/motor_topic', self.encoder_callback, 10)

        self.received_cmd = None
        self.actual_linear_v = 0.0
        self.actual_angular_v = 0.0

        # **ROS2 Timer를 사용하여 주기 조정**
        self.create_timer(self.dt, self.predict)  # 10Hz (100ms)
        self.create_timer(0.1, self.publish_corrected_cmd)  # 10Hz (100ms)

    def cmd_vel_callback(self, msg):
        """ 사용자가 입력한 원래 cmd_vel 저장 """
        self.received_cmd = msg

    def predict(self):
        """ EKF 예측 단계 """
        if self.received_cmd is None:
            return

        linear_v = self.received_cmd.linear.x
        angular_v = self.received_cmd.angular.z
        theta = self.state[2]

        # 상태 업데이트
        self.state[0] += self.state[3] * self.dt
        self.state[1] += self.state[4] * self.dt
        self.state[2] += self.state[5] * self.dt
        self.state[3] = linear_v * np.cos(theta)
        self.state[4] = linear_v * np.sin(theta)
        self.state[5] = angular_v

        # 공분산 업데이트
        A_t = np.eye(6)
        A_t[0, 3] = self.dt
        A_t[1, 4] = self.dt
        A_t[2, 5] = self.dt

        self.P = A_t @ self.P @ A_t.T + self.Q

    def encoder_callback(self, msg):
        """ EKF 업데이트: 엔코더 기반 실제 속도 보정 """
        theta = self.state[2]
        omega_L = msg.left_w
        omega_R = msg.right_w

        # 이동 거리 및 회전각 계산
        D_L = omega_L * (self.D / 2) * self.dt
        D_R = omega_R * (self.D / 2) * self.dt
        D = (D_L + D_R) / 2
        delta_theta = (D_R - D_L) / self.L

        delta_x = D * np.cos(theta)
        delta_y = D * np.sin(theta)

        # 측정 벡터 계산 및 EKF 업데이트
        H = np.zeros((3, 6))
        H[:, 3:6] = np.eye(3) * self.dt
        z = np.array([delta_x, delta_y, delta_theta])
        y = z - H @ self.state
        S = H @ self.P @ H.T + self.R
        K = self.P @ H.T @ np.linalg.inv(S)
        self.state += K @ y
        self.P = (np.eye(6) - K @ H) @ self.P

        self.actual_linear_v = np.sqrt(self.state[3]**2 + self.state[4]**2)
        self.actual_angular_v = self.state[5]

    def publish_corrected_cmd(self):
        """ 보정된 cmd_vel 송신 """
        if self.received_cmd is None:
            return

        corrected_cmd = Twist()
        corrected_cmd.linear.x = self.received_cmd.linear.x + (self.received_cmd.linear.x - self.actual_linear_v)
        corrected_cmd.angular.z = self.received_cmd.angular.z + (self.received_cmd.angular.z - self.actual_angular_v)

        self.cmd_vel_pub.publish(corrected_cmd)
        self.get_logger().info(f"Corrected cmd_vel: linear_v={corrected_cmd.linear.x:.3f}, angular_v={corrected_cmd.angular.z:.3f}")

def main(args=None):
    rclpy.init(args=args)
    node = EKF()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt: 
        node.destroy_node()
        rclpy.shutdown()
    
if __name__ == "__main__":
    main()