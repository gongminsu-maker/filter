
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 모터 -> 오도메트리 변환 노드 실행
        # R_t 계산 노드 실행
        Node(
            package='mobile_robot_pkg',
            executable='cmd',
            output='screen'
           
        ),
        Node(
            package='mobile_robot_pkg',
            executable='odom',
            output='screen'
           
        ),
        # cmd_vel 입력 노드 실행
        Node(
            package='mobile_robot_pkg',
            executable='kalman_filter',
            output='screen'
        ),
    ])
