#include <franka/exception.h>
#include <franka/gripper.h>
#include <franka/robot.h>
#include <iostream>
#include <chrono>
#include <thread>
#include <math.h>
#include <franka/duration.h>
#include <franka/exception.h>
#include "examples_common.h"

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <robot-hostname>" << std::endl;
        return -1;
    }
    try {
        franka::Robot robot(argv[1]);
        double time = 0.0;
        setDefaultBehavior(robot);
        std::array<double, 7> initial_joint_position = {{0, -M_PI_4, 0, -3 * M_PI_4, 0, M_PI_2, M_PI_4}};
        std::array<double, 16> cart_position;
        MotionGenerator motion_generator(0.3, initial_joint_position);
        std::cout << "Reseting robot to HOME position "
                  << "Please make sure to have the user stop button at hand!" << std::endl
                  << "Press Enter to continue..." << std::endl;
        std::cin.ignore();
        robot.control(motion_generator);
        std::cout << "Finished moving to initial joint configuration." << std::endl << std::endl;
        std::cout << "Starting Joint control test." << std::endl;

        robot.setCollisionBehavior(
                {{20.0, 20.0, 18.0, 18.0, 16.0, 14.0, 12.0}}, {{20.0, 20.0, 18.0, 18.0, 16.0, 14.0, 12.0}},
                {{20.0, 20.0, 18.0, 18.0, 16.0, 14.0, 12.0}}, {{20.0, 20.0, 18.0, 18.0, 16.0, 14.0, 12.0}},
                {{20.0, 20.0, 20.0, 25.0, 25.0, 25.0}}, {{20.0, 20.0, 20.0, 25.0, 25.0, 25.0}},
                {{20.0, 20.0, 20.0, 25.0, 25.0, 25.0}}, {{20.0, 20.0, 20.0, 25.0, 25.0, 25.0}});

        //franka::Torques zero_torques{{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0}};
        std::cout << "Press Enter to continue..." << std::endl;
        std::cin.ignore();
        robot.control([&cart_position, &time](const franka::RobotState& robot_state, franka::Duration period) -> franka::CartesianPose
          {
              time += period.toSec();
              if (time == 0.0) {
                  cart_position = robot_state.O_T_EE_c;
              }
              std::cout << "Time" << time << std::endl;
              //double delta_z = 0.2 * (cos(M_PI/4 * (1 - cos(M_PI/5 * time))) -1);
              double delta_z = 0.2*(std::cos(M_PI/4*(1-std::cos(M_PI/5*time)))-1);
              std::array<double, 16> new_cart_position = cart_position;
              new_cart_position[14] = new_cart_position[14] + delta_z;
              if (time>=20)
                  return franka::MotionFinished(new_cart_position);
              return new_cart_position;
          });
    }catch (const franka::Exception& e) {
        std::cout << e.what() << std::endl;
        return -1;
    }
    return 0;
}

