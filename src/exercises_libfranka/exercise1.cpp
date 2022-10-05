#include <franka/exception.h>
#include <franka/gripper.h>
#include <franka/robot.h>
#include <iostream>
#include "examples_common.h"
#include <franka/gripper.h>
#include <time.h>

int main(int argc, char** argv)
{
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <robot-hostname>" << std::endl;
        return -1;
    }
    try {
        double width = 0.07;
        double speed = 0.01;
        bool status = false;
        franka::Robot robot(argv[1]);
        franka::Gripper gripper(argv[1]);
        franka::GripperState gs;
        //setDefaultBehavior(robot);
        std::cout << "Starting Gripper Action." << std::endl;
        gripper.move(width, speed);

        while (status!=true) {
            gs = gripper.readOnce();
            std::cout << "Gripper moving !!" << std::endl;

        }
        std::cout << "Done";
    } catch (const franka::Exception& e) {
        std::cout << e.what() << std::endl;
        return -1;
    }
    return 0;
}

