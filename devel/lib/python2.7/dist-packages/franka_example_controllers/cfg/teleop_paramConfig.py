## *********************************************************
##
## File autogenerated for the franka_example_controllers package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'CONTROLLER_GAINS', 'lower': 'controller_gains', 'srcline': 124, 'name': 'Controller_Gains', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::CONTROLLER_GAINS', 'field': 'DEFAULT::controller_gains', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 11, 'description': 'Factor to be multiplied with initial leader d_gains', 'max': 8.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'leader_damping_scaling', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 15, 'description': 'Factor to be multiplied with initial p-gains of follower arm, damping will also be adapted', 'max': 1.3, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'follower_stiffness_scaling', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.1, 'type': 'double'}], 'type': 'apply', 'id': 1}, {'upper': 'FORCE_FEEDBACK', 'lower': 'force_feedback', 'srcline': 124, 'name': 'Force_Feedback', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::FORCE_FEEDBACK', 'field': 'DEFAULT::force_feedback', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 20, 'description': 'Applied feedback force when leader arm is idle', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'force_feedback_idle', 'edit_method': '', 'default': 0.5, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 23, 'description': 'Applied feedback force when leader arm is guided', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'force_feedback_guiding', 'edit_method': '', 'default': 0.98, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 2}, {'upper': 'CARTESIAN_CONTACT', 'lower': 'cartesian_contact', 'srcline': 124, 'name': 'Cartesian_Contact', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::CARTESIAN_CONTACT', 'field': 'DEFAULT::cartesian_contact', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 29, 'description': 'Force threshold at leader endeffector to determine whether the arm is in contact.', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'leader_contact_force_threshold', 'edit_method': '', 'default': 4.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 33, 'description': 'Force threshold at follower endeffector to determine whether the arm is in contact.', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'follower_contact_force_threshold', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 0.1, 'type': 'double'}], 'type': '', 'id': 3}, {'upper': 'MAX_VELOCITIES', 'lower': 'max_velocities', 'srcline': 124, 'name': 'Max_Velocities', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::MAX_VELOCITIES', 'field': 'DEFAULT::max_velocities', 'state': True, 'parentclass': 'DEFAULT', 'groups': [{'upper': 'DQ_MAXLOWER', 'lower': 'dq_maxlower', 'srcline': 124, 'name': 'Dq_MaxLower', 'parent': 4, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Max_Velocities', 'class': 'DEFAULT::MAX_VELOCITIES::DQ_MAXLOWER', 'field': 'DEFAULT::MAX_VELOCITIES::dq_maxlower', 'state': True, 'parentclass': 'DEFAULT::MAX_VELOCITIES', 'groups': [{'upper': 'DQ_MAX_LOWER', 'lower': 'dq_max_lower', 'srcline': 124, 'name': 'dq_max_lower', 'parent': 5, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Dq_MaxLower', 'class': 'DEFAULT::MAX_VELOCITIES::DQ_MAXLOWER::DQ_MAX_LOWER', 'field': 'DEFAULT::MAX_VELOCITIES::DQ_MAXLOWER::dq_max_lower', 'state': True, 'parentclass': 'DEFAULT::MAX_VELOCITIES::DQ_MAXLOWER', 'groups': [], 'parameters': [{'srcline': 39, 'description': 'Description', 'max': 2.17, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_l_1', 'edit_method': '', 'default': 0.8, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 40, 'description': 'Description', 'max': 2.17, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_l_2', 'edit_method': '', 'default': 0.8, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 41, 'description': 'Description', 'max': 2.17, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_l_3', 'edit_method': '', 'default': 0.8, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 42, 'description': 'Description', 'max': 2.17, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_l_4', 'edit_method': '', 'default': 0.8, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 43, 'description': 'Description', 'max': 2.6, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_l_5', 'edit_method': '', 'default': 2.5, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 44, 'description': 'Description', 'max': 2.6, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_l_6', 'edit_method': '', 'default': 2.5, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 45, 'description': 'Description', 'max': 2.6, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_l_7', 'edit_method': '', 'default': 2.5, 'level': 0, 'min': 0.1, 'type': 'double'}], 'type': 'apply', 'id': 6}], 'parameters': [], 'type': 'tab', 'id': 5}, {'upper': 'DQ_MAXUPPER', 'lower': 'dq_maxupper', 'srcline': 124, 'name': 'Dq_MaxUpper', 'parent': 4, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Max_Velocities', 'class': 'DEFAULT::MAX_VELOCITIES::DQ_MAXUPPER', 'field': 'DEFAULT::MAX_VELOCITIES::dq_maxupper', 'state': True, 'parentclass': 'DEFAULT::MAX_VELOCITIES', 'groups': [{'upper': 'DQ_MAX_UPPER', 'lower': 'dq_max_upper', 'srcline': 124, 'name': 'dq_max_upper', 'parent': 7, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Dq_MaxUpper', 'class': 'DEFAULT::MAX_VELOCITIES::DQ_MAXUPPER::DQ_MAX_UPPER', 'field': 'DEFAULT::MAX_VELOCITIES::DQ_MAXUPPER::dq_max_upper', 'state': True, 'parentclass': 'DEFAULT::MAX_VELOCITIES::DQ_MAXUPPER', 'groups': [], 'parameters': [{'srcline': 49, 'description': 'Description', 'max': 2.17, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_u_1', 'edit_method': '', 'default': 2.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 50, 'description': 'Description', 'max': 2.17, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_u_2', 'edit_method': '', 'default': 2.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 51, 'description': 'Description', 'max': 2.17, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_u_3', 'edit_method': '', 'default': 2.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 52, 'description': 'Description', 'max': 2.17, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_u_4', 'edit_method': '', 'default': 2.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 53, 'description': 'Description', 'max': 2.6, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_u_5', 'edit_method': '', 'default': 2.5, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 54, 'description': 'Description', 'max': 2.6, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_u_6', 'edit_method': '', 'default': 2.5, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 55, 'description': 'Description', 'max': 2.6, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'dq_u_7', 'edit_method': '', 'default': 2.5, 'level': 0, 'min': 0.1, 'type': 'double'}], 'type': 'apply', 'id': 8}], 'parameters': [], 'type': 'tab', 'id': 7}], 'parameters': [], 'type': '', 'id': 4}, {'upper': 'MAX_ACCELERATION', 'lower': 'max_acceleration', 'srcline': 124, 'name': 'Max_Acceleration', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::MAX_ACCELERATION', 'field': 'DEFAULT::max_acceleration', 'state': True, 'parentclass': 'DEFAULT', 'groups': [{'upper': 'DDQ_MAXLOWER', 'lower': 'ddq_maxlower', 'srcline': 124, 'name': 'Ddq_MaxLower', 'parent': 9, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Max_Acceleration', 'class': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXLOWER', 'field': 'DEFAULT::MAX_ACCELERATION::ddq_maxlower', 'state': True, 'parentclass': 'DEFAULT::MAX_ACCELERATION', 'groups': [{'upper': 'DDQ_MAX_LOWER', 'lower': 'ddq_max_lower', 'srcline': 124, 'name': 'ddq_max_lower', 'parent': 10, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Ddq_MaxLower', 'class': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXLOWER::DDQ_MAX_LOWER', 'field': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXLOWER::ddq_max_lower', 'state': True, 'parentclass': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXLOWER', 'groups': [], 'parameters': [{'srcline': 60, 'description': 'Description', 'max': 15.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_l_1', 'edit_method': '', 'default': 0.8, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 61, 'description': 'Description', 'max': 7.5, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_l_2', 'edit_method': '', 'default': 0.8, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 62, 'description': 'Description', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_l_3', 'edit_method': '', 'default': 0.8, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 63, 'description': 'Description', 'max': 12.5, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_l_4', 'edit_method': '', 'default': 0.8, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 64, 'description': 'Description', 'max': 15.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_l_5', 'edit_method': '', 'default': 10.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 65, 'description': 'Description', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_l_6', 'edit_method': '', 'default': 10.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 66, 'description': 'Description', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_l_7', 'edit_method': '', 'default': 10.0, 'level': 0, 'min': 0.1, 'type': 'double'}], 'type': 'apply', 'id': 11}], 'parameters': [], 'type': 'tab', 'id': 10}, {'upper': 'DDQ_MAXUPPER', 'lower': 'ddq_maxupper', 'srcline': 124, 'name': 'Ddq_MaxUpper', 'parent': 9, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Max_Acceleration', 'class': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXUPPER', 'field': 'DEFAULT::MAX_ACCELERATION::ddq_maxupper', 'state': True, 'parentclass': 'DEFAULT::MAX_ACCELERATION', 'groups': [{'upper': 'DDQ_MAX_UPPER', 'lower': 'ddq_max_upper', 'srcline': 124, 'name': 'ddq_max_upper', 'parent': 12, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Ddq_MaxUpper', 'class': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXUPPER::DDQ_MAX_UPPER', 'field': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXUPPER::ddq_max_upper', 'state': True, 'parentclass': 'DEFAULT::MAX_ACCELERATION::DDQ_MAXUPPER', 'groups': [], 'parameters': [{'srcline': 70, 'description': 'Description', 'max': 15.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_u_1', 'edit_method': '', 'default': 6.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 71, 'description': 'Description', 'max': 7.5, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_u_2', 'edit_method': '', 'default': 6.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 72, 'description': 'Description', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_u_3', 'edit_method': '', 'default': 6.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 73, 'description': 'Description', 'max': 12.5, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_u_4', 'edit_method': '', 'default': 6.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 74, 'description': 'Description', 'max': 15.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_u_5', 'edit_method': '', 'default': 15.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 75, 'description': 'Description', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_u_6', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 76, 'description': 'Description', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/ros/transformations_ws/src/franka_ros/franka_example_controllers/cfg/teleop_param.cfg', 'name': 'ddq_u_7', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.1, 'type': 'double'}], 'type': 'apply', 'id': 13}], 'parameters': [], 'type': 'tab', 'id': 12}], 'parameters': [], 'type': '', 'id': 9}], 'parameters': [], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

