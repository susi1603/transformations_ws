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
        double time = 0;
        setDefaultBehavior(robot);
        std::array<double, 7> initial_position = {{0, -M_PI_4, 0, -3 * M_PI_4, 0, M_PI_2, M_PI_4}};
        MotionGenerator motion_generator(0.3, initial_position);
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
        double des_time;
        std::cout << "Enter Duration in seconds: "; // Type a number and press enter
        std::cin >> des_time; // Get user input from the keyboard
        std::cout << "Press Enter to continue..." << std::endl;
        std::cin.ignore();
        robot.control([&initial_position, &time, &des_time](const franka::RobotState& robot_state, franka::Duration period) -> franka::JointPositions
                      {
                          time += period.toSec();
                          if (time == 0.0) {
                              initial_position = robot_state.q_d;
                          }
                          double delta_angle = M_PI/8 * (1-cos(M_PI/2.5*time));
                          std::cout << "Delta angle " << delta_angle << std::endl;
                          std::cout << "Time " << time << std::endl;
                          franka::JointPositions output = {{initial_position[0], initial_position[1],
                                                            initial_position[2], initial_position[3],
                                                            initial_position[4], initial_position[5] + delta_angle,
                                                            initial_position[6]}};
                          if (time>=des_time)
                              return franka::MotionFinished(output);
                          return output;
                      });
    }catch (const franka::Exception& e) {
        std::cout << e.what() << std::endl;
        return -1;
    }
    return 0;
}

