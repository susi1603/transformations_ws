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
#include <franka/model.h>

using Vector7 = Eigen::Matrix<double, 7, 1>;

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <robot-hostname>" << std::endl;
        return -1;
    }

    try {
        double time = 0.0;
        franka::Robot robot(argv[1]);
        setDefaultBehavior(robot);
        std::array<double, 7> initial_joint_position = {{0, -M_PI_4, 0, -3 * M_PI_4, 0, M_PI_2, M_PI_4}};
        MotionGenerator motion_generator(0.3, initial_joint_position);
        std::cout << "Reseting robot to HOME position "
                  << "Please make sure to have the user stop button at hand!" << std::endl
                  << "Press Enter to continue..." << std::endl;
        std::cin.ignore();
        robot.setCollisionBehavior(
                {{100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0}}, {{100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0}},
                {{100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0}}, {{100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0}},
                {{100.0, 100.0, 100.0, 100.0, 100.0, 100.0}}, {{100.0, 100.0, 100.0, 100.0, 100.0, 100.0}},
                {{100.0, 100.0, 100.0, 100, 100.0, 100.0}}, {{100.0, 100.0, 100.0, 100.0, 100.0, 100.0}});


        std::cout << "Starting Torque control" << std::endl;
        franka::Model model = robot.loadModel();
        robot.control([&model](const franka::RobotState& robot_state, franka::Duration period) -> franka::Torques
        {
            Eigen::Map<const Vector7> coriolis(model.coriolis(robot_state).data());
            Eigen::Map<const Vector7> q(robot_state.q.data());
            Eigen::Map<const Vector7> dq(robot_state.dq.data());
            Vector7 p_gains, d_gains, computed_torques;
            Vector7 q_desired;
            //p_gains << 600.0, 600.0, 600.0, 600.0, 250.0, 150.0, 50.0;
            p_gains << 30.0, 30.0, 30.0, 30.0, 12.5, 7.5, 2.5;
            d_gains << 5.0, 5.0, 5.0, 5.0, 3.0, 2.5, 1.5;
            q_desired << 0, -M_PI_4, 0, -3 * M_PI_4, 0, M_PI_2, M_PI_4;
            computed_torques = p_gains.cwiseProduct(q_desired-q)  + d_gains.cwiseProduct(-dq)+coriolis;
            // Converting vector to Matrix
            std::array<double, 7> torques{};
            Vector7::Map(&torques[0]) = computed_torques;

            return torques;
          });
    }catch (const franka::Exception& e)
    {
        std::cout << e.what() << std::endl;
    }

    return 0;
}

