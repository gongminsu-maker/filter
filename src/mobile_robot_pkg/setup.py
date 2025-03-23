from setuptools import find_packages, setup
import os
import glob

package_name = 'mobile_robot_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch','*.launch.*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gongminsu',
    maintainer_email='gongminsu@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "kalman_encoder=mobile_robot_pkg.kalman_encoder:main",
            "odom=mobile_robot_pkg.odom:main",
            "cov=mobile_robot_pkg.cov:main",
            "cmd=mobile_robot_pkg.cmd:main",
            "cov_3=mobile_robot_pkg.cov_3:main",
            "imu_odom=mobile_robot_pkg.imu_odom:main",
            "kalman_filter=mobile_robot_pkg.kalman_filter:main",
            "kalman_filter_yaw=mobile_robot_pkg.kalman_filter_yaw:main",
            "test=mobile_robot_pkg.test:main",
            "accel=mobile_robot_pkg.accel:main",
            "squarecontrol = mobile_robot_pkg.squarecontrol:main",

        ],
    },
)
