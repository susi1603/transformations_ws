#include <franka/exception.h>
#include <franka/gripper.h>
#include <franka/model.h>
#include <franka/robot.h>
#include <iostream>
#include <iterator>

template <class T, size_t N>
std::ostream& operator<<(std::ostream& ostream, const std::array<T, N>& array) {
    ostream << "[";
    std::copy(array.cbegin(), array.cend() - 1, std::ostream_iterator<T>(ostream, ","));
    std::copy(array.cend() - 1, array.cend(), std::ostream_iterator<T>(ostream));
    ostream << "]";
    return ostream;
}

int main(int argc, char** argv) {
    franka::Robot robot(argv[1]);
    franka::RobotState state = robot.readOnce();
    size_t count = 0;
    std::cout << "Starting to read robot state" << std::endl;
    franka::Model model(robot.loadModel());
    for (franka::Frame frame = franka::Frame::kJoint1; frame <= franka::Frame::kEndEffector; frame++)
    {
        std::cout << model.pose(frame, state) << std::endl;
    }
    std::cout << "Finished reading robot state" << std::endl;
    do {
        std::cout << "Press any key to continue..." << std::endl;
    }while (std::cin.get() != '\n');
    franka::Gripper gripper(argv[1]);
    double width = 0.05;
    double speed = 0.03;
    bool status;
    gripper.move(width, speed);
    std::cout << "Done" << std::endl;
  return 0;
}

