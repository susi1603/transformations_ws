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
#include <string>

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
        std::array<double, 2> elbow_position;
        std::array<double, 16> cart_position;
        franka::Gripper gripper(argv[1]);
        MotionGenerator motion_generator(0.3, initial_joint_position);
        std::cout << "Reseting robot to HOME position "
                  << "Please make sure to have the user stop button at hand!" << std::endl
                  << "Press Enter to continue..." << std::endl;
        std::cin.ignore();
        std::string choice;
        std::cout << "Do you want gripper homing ? "; //
        std::cin >> choice; // Get user input from the keyboard
        if(std::strcmp(choice.c_str(), "yes") == 1)
        {
            std::cout << "Starting Gripper Homing." << std::endl;
            gripper.homing();
            robot.automaticErrorRecovery();
        }
        double width = 0.07;
        double speed = 0.1;
        gripper.move(width, speed);
        std::cout << "Gripper moved" << std::endl;

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
        robot.control([&cart_position, &elbow_position, &time](const franka::RobotState& robot_state, franka::Duration period) -> franka::CartesianPose
                      {
                          time += period.toSec();
                          int flag = 0;
                          if (time == 0.0) {
                              cart_position = robot_state.O_T_EE_c;
                              elbow_position = robot_state.elbow_c;
                          }
                          std::cout << "Time" << time << std::endl;
                          //double delta_z = 0.2 * (cos(M_PI/4 * (1 - cos(M_PI/5 * time))) -1);
                          double delta_angle = M_PI/15 * (1 - cos(M_PI/5 *time));
                          std::array<double, 2> new_elbow_position = elbow_position;
                          new_elbow_position[0] = new_elbow_position[0] + delta_angle;
                          /*if(flag == 0) {
                              new_elbow_position[1] = -new_elbow_position[1];
                              flag = 1;
                          }*/
                          if (time>=1)
                              return franka::MotionFinished({cart_position, new_elbow_position});
                          return {cart_position, new_elbow_position};
                      });
        gripper.move(0, speed);
    }catch (const franka::Exception& e) {
        std::cout << e.what() << std::endl;
        return -1;
    }
    return 0;
}



