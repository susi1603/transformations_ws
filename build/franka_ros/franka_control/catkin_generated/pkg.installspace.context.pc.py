# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/home/airocs/libfranka/include".split(';') if "${prefix}/include;/home/airocs/libfranka/include" != "" else []
PROJECT_CATKIN_DEPENDS = "controller_interface;franka_hw;franka_msgs;geometry_msgs;pluginlib;realtime_tools;roscpp;sensor_msgs;tf2_msgs;std_srvs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lfranka_state_controller;/home/airocs/libfranka/build/libfranka.so.0.8.0".split(';') if "-lfranka_state_controller;/home/airocs/libfranka/build/libfranka.so.0.8.0" != "" else []
PROJECT_NAME = "franka_control"
PROJECT_SPACE_DIR = "/home/airocs/ros/transformations_ws/install"
PROJECT_VERSION = "0.8.0"
