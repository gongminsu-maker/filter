import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/gongminsu/mobile_robot/install/mobile_robot_pkg'
