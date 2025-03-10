import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import os
import pandas as pd

class CmdVelController(Node):
    def __init__(self):
        super().__init__('accel_sub')

        self.cmd_vel_publisher = self.create_subscription(Imu, '/imu/data',self.sub_callback, 10)
        self.last_time = self.get_clock().now() 
        self.x = 0
        self.vx = 0
        self.vy = 0

        self.log_data =[]

    def sub_callback(self,msg):
        self.current_time = self.get_clock().now()
        dt = (self.current_time - self.last_time).nanoseconds/1e9

        ax = -msg.linear_acceleration.x
        ay = -msg.linear_acceleration.y
        self.vx += ax*dt
        self.vy += ay*dt
        self.x += self.vx*dt + (ax*dt*dt)/2
        self.get_logger().info(f"{ax},{ay},{self.vx},{self.vy},{self.x}")

        self.last_time = self.current_time


        self.log_data.append([self.vx,self.vy,ax,ay,self.x])
        self.save_to_excel()


    def save_to_excel(self):
        df = pd.DataFrame(self.log_data, columns=['vx','vy','ax','ay','self.x'])
        file_path = os.path.join(os.getcwd(), "sensor_fusion_log.xlsx")
        df.to_excel(file_path, index=False, engine='openpyxl')
        print(f"[📂] 데이터 저장 완료: {file_path}")



def main(args=None):
    rclpy.init(args=args)
    node = CmdVelController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
