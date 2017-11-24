# environment constants:
number_of_agvs = 2
number_of_agv_motors = 2  # 0 = leftMotor, 1 = rightMotor
initial_motor_speed = 0.4
distance_to_goal = 0
wheel_radius = 0.0275
wheels_separation = 0.4
factory_width = 60  # x0.5m in 1 square
factory_length = 120  # x0.5m in 1 square
cell_length = 0.5
cell_bias = 0.225
simulation_iterations = 1

# handles lists:
agv_handles = [0 for _ in range(number_of_agvs)]
motor_handles = [[0 for _ in range(number_of_agv_motors)] for _ in range(number_of_agvs)]

# parameters:
factory_floor = [[0 for _ in range(factory_width)] for _ in range(factory_length)]
agv = [0 for _ in range(number_of_agvs)]  # has agv data - position and orientation
agv_transformation_matrices = [0 for _ in range(number_of_agvs)]
get_agv_velocities = [0 for _ in range(number_of_agvs)]
set_agv_velocities = [[0 for _ in range(number_of_agv_motors)] for _ in range(number_of_agvs)]

# environment:
environment_objects = ['Pioneer_p3dx_visible', 'box', 'control_centre', 'Cuboid', 'wall_1', 'wall_2', 'wall_3',
                       'wall_4', 'wall_5', 'wall_6', 'customizableConveyor', 'Cuboid0', 'Cuboid1',
                       'Cuboid2', 'Cuboid3']
dynamical_objects_cells = [0 for _ in range(number_of_agvs)]
number_of_racks = 168
for i in range(number_of_racks):
    environment_objects.append('rack' + str(i + 1))
for i in range(number_of_agvs):
    environment_objects.append('agv_' + str(i + 1))
number_of_environment_objects = len(environment_objects)
environment_objects_handles = []
get_environment_objects_data = [0 for _ in range(number_of_environment_objects)]
wall_12_start = 20
wall_12_end = 60
wall_3_start = 0
wall_3_end = 120
wall_4_start = 80
wall_4_end = 110
wall_5_start = 10
wall_5_end = 40
wall_6_start = 50
wall_6_end = 70
wall_1_x_point = 0
wall_2_x_point = 119
wall_3_y_point = 59
wall_456_y_point = 20

# collision avoidance parameters:
number_of_proximity_sensors = 16
sensors_counter = 0
agv_sensors_handles = {'agv_1': [0 for _ in range(number_of_proximity_sensors)],
                       'agv_2': [0 for _ in range(number_of_proximity_sensors)]}
agv_sensors_read_data = {'agv_1': [0 for _ in range(number_of_proximity_sensors)],
                         'agv_2': [0 for _ in range(number_of_proximity_sensors)]}
agv_sensors_detection = {'agv_1': [0 for _ in range(number_of_proximity_sensors)],
                         'agv_2': [0 for _ in range(number_of_proximity_sensors)]}
# agv_sensors_handles = {'agv_1': [0 for _ in range(number_of_proximity_sensors)]}
# agv_sensors_read_data = {'agv_1': [0 for _ in range(number_of_proximity_sensors)]}
# agv_sensors_detection = {'agv_1': [0 for _ in range(number_of_proximity_sensors)]}
detect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
braitenberg_left = [-0.2, -0.4, -0.6, -0.8, -1, -1.2, -1.4, -1.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
braitenberg_right = [-1.6, -1.4, -1.2, -1, -0.8, -0.6, -0.4, -0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
no_detection_dist = 0.5
max_detection_dist = 0.2

# pathfinder planner parameters:
d = [0 for _ in range(number_of_agvs)]  # distance to points for each agv
k = [0 for _ in range(number_of_agvs)]  # bezier point for each agv
path = [0 for _ in range(number_of_agvs)]  # path for each agv

# PD controller parameter:
# Kp = 0.4
# Kd = 0.8
last_phi = [0 for _ in range(number_of_agvs)]
Kp = - 0.4
Kd = - 1.6
Kv = 0
# Kv = 0.002

# static environment handles and parameters:
environment_objects_handles = [186, 172, 158, 214, 219, 218, 217, 216, 215, 15, 159, 220, 221, 222, 223, 347, 350, 353, 356, 359, 362, 365, 368, 371, 374, 377, 380, 383, 386, 389, 392, 395, 398, 401, 404, 407, 410, 413, 416, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 265, 306]
get_environment_objects_data = [{'x': -29.804935455322266, 'y': -13.666674613952637, 'z': 0.15731704235076904, 'a': -0.00615441519767046, 'b': 0.00022113545855972916, 'g': -1.5908905267715454}, {'x': -4.579997539520264, 'y': -8.99999713897705, 'z': 0.034999921917915344, 'a': 1.0305217096329145e-10, 'b': 8.807656270981568e-10, 'g': -1.246986958136631e-10}, {'x': 27.5, 'y': -12.499999046325684, 'z': 0.9999997019767761, 'a': -1.9168029385951968e-09, 'b': 1.5448058832134848e-08, 'g': 2.8455620082468158e-08}, {'x': -29.2549991607666, 'y': -13.299992561340332, 'z': 0.09999991953372955, 'a': 1.735161875293656e-10, 'b': -4.6072586717960107e-11, 'g': -1.6736093066960223e-10}, {'x': -29.950000762939453, 'y': 5.000003337860107, 'z': 0.24998527765274048, 'a': 1.0132789611816406e-06, 'b': -1.1920928955078125e-07, 'g': 6.039613253960852e-14}, {'x': 29.949975967407227, 'y': 5.000002861022949, 'z': 0.24999673664569855, 'a': 1.0132789611816406e-06, 'b': -1.1920928955078125e-07, 'g': 6.039613253960852e-14}, {'x': -4.589557647705078e-06, 'y': 14.94999885559082, 'z': 0.2500011920928955, 'a': 1.1026859283447266e-06, 'b': -1.788139627478813e-07, 'g': -5.960453819398026e-08}, {'x': 17.500001907348633, 'y': -4.949995040893555, 'z': 0.2499852180480957, 'a': 1.1026859283447266e-06, 'b': -1.788139627478813e-07, 'g': -5.960453819398026e-08}, {'x': -17.499996185302734, 'y': -4.949995040893555, 'z': 0.24997949600219727, 'a': 1.1026859283447266e-06, 'b': -1.788139627478813e-07, 'g': -5.960453819398026e-08}, {'x': -5.066394805908203e-06, 'y': -4.949993133544922, 'z': 0.24998092651367188, 'a': 1.1026859283447266e-06, 'b': -1.788139627478813e-07, 'g': -5.960453819398026e-08}, {'x': -5.124999523162842, 'y': -8.399999618530273, 'z': 0.36000001430511475, 'a': -0.0, 'b': 0.0, 'g': -0.0}, {'x': -28.704998016357422, 'y': -13.274991989135742, 'z': 0.09999991953372955, 'a': 1.4202150566688942e-10, 'b': 5.930719804148055e-11, 'g': -1.112408290482314e-10}, {'x': -27.7549991607666, 'y': -13.774996757507324, 'z': 0.09999991953372955, 'a': -8.378637367245645e-11, 'b': -1.4213585863842582e-10, 'g': 8.680794277848847e-11}, {'x': -28.279998779296875, 'y': -12.799994468688965, 'z': 0.09999991953372955, 'a': -4.9067711699324335e-11, 'b': -4.8111705591713516e-11, 'g': -7.42633107786439e-11}, {'x': -29.830001831054688, 'y': -13.274991989135742, 'z': 0.09999991953372955, 'a': 1.1280463368956717e-10, 'b': 5.2021140867219984e-11, 'g': -6.854650874688062e-11}, {'x': -24.200000762939453, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -24.200000762939453, 'y': -0.6999976634979248, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -22.20001792907715, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -22.20001792907715, 'y': -0.6999976634979248, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -20.275007247924805, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -20.275007247924805, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -24.200000762939453, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -22.20001792907715, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -20.275007247924805, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -24.200000762939453, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -22.20001792907715, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -20.275007247924805, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -24.200000762939453, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -22.20001792907715, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -20.275007247924805, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -24.200000762939453, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -22.20001792907715, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -20.275007247924805, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -24.200000762939453, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -22.20001792907715, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -20.275007247924805, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -24.200000762939453, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -22.20001792907715, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -20.275007247924805, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -18.174976348876953, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -18.174976348876953, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -16.17499542236328, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -14.249873161315918, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -18.174976348876953, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -16.17499542236328, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -14.249873161315918, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -18.174976348876953, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -16.17499542236328, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -14.249873161315918, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -18.174976348876953, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -18.174976348876953, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -16.17499542236328, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -14.249873161315918, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -18.174976348876953, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -16.17499542236328, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -14.249873161315918, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -16.17499542236328, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -16.17499542236328, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -14.249873161315918, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -14.249873161315918, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -18.174976348876953, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -16.17499542236328, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -14.249873161315918, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -12.200093269348145, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -10.274971008300781, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -10.274971008300781, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -12.200093269348145, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -12.200093269348145, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -10.274971008300781, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -10.274971008300781, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -12.200093269348145, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -12.200093269348145, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -10.274971008300781, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -10.274971008300781, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -12.200093269348145, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -12.200093269348145, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -10.274971008300781, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -12.200093269348145, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -10.274873733520508, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -4.250003814697266, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -2.25001859664917, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -0.3250093460083008, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 1.7750203609466553, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 3.7750020027160645, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -4.250003814697266, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -2.25001859664917, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -0.3250093460083008, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 1.7750203609466553, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 3.7750020027160645, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -4.250003814697266, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -2.25001859664917, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -0.3250093460083008, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 1.7750203609466553, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 3.7750020027160645, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -4.250003814697266, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -2.25001859664917, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -0.3250093460083008, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 1.7750203609466553, 'y': 4.224999904632568, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 3.7750020027160645, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -4.250003814697266, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -2.25001859664917, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -0.3250093460083008, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 1.7750203609466553, 'y': 6.725000381469727, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 3.7750020027160645, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -4.250003814697266, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -2.25001859664917, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -0.3250093460083008, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 1.7750203609466553, 'y': 9.29999828338623, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 3.7750020027160645, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -4.250003814697266, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -2.25001859664917, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -0.3250093460083008, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 1.7750203609466553, 'y': 11.749995231628418, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 3.7750020027160645, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -4.250003814697266, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -2.25001859664917, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': -0.3250093460083008, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 1.7750203609466553, 'y': 14.224994659423828, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 3.7750039100646973, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 10.824947357177734, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 12.824934005737305, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 14.749942779541016, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 16.849998474121094, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 18.849979400634766, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 20.775104522705078, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 22.82488250732422, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 24.75000762939453, 'y': -3.2499988079071045, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 24.75000762939453, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 22.82488250732422, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 20.775104522705078, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 16.849998474121094, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 18.849979400634766, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 14.749942779541016, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 12.824934005737305, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 10.824947357177734, 'y': -0.6999989151954651, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 10.824947357177734, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 12.824934005737305, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 14.749942779541016, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 16.849998474121094, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 18.849979400634766, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 20.775104522705078, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 22.82488250732422, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 24.75000762939453, 'y': 1.800000786781311, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 24.75000762939453, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 22.82488250732422, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 20.775104522705078, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 18.849979400634766, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 16.849998474121094, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 14.749942779541016, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 12.824934005737305, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 10.824947357177734, 'y': 4.224926471710205, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 10.824947357177734, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 12.824934005737305, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 14.749942779541016, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 16.849998474121094, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 18.849979400634766, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 20.775104522705078, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 22.82488250732422, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 24.75000762939453, 'y': 6.724926948547363, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 24.75000762939453, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 22.82488250732422, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 20.775104522705078, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 18.849979400634766, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 16.849998474121094, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 14.749942779541016, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 12.824934005737305, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 10.824947357177734, 'y': 9.299924850463867, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 10.824947357177734, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 12.824934005737305, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 14.749942779541016, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 16.849998474121094, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 18.849979400634766, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 20.775104522705078, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 22.82488250732422, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 24.75000762939453, 'y': 11.749921798706055, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 24.750102996826172, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 22.82488250732422, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 20.775104522705078, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 18.849979400634766, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 16.849998474121094, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 14.749942779541016, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 12.824934005737305, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 10.82499885559082, 'y': 14.224992752075195, 'z': 0.8550000190734863, 'a': 2.861005441445741e-06, 'b': 4.76838204122032e-06, 'g': 7.390968676190823e-06}, {'x': 0.7061657905578613, 'y': -11.149299621582031, 'z': 0.13864359259605408, 'a': 0.0001836889423429966, 'b': 0.0030172280967235565, 'g': 3.106250524520874}, {'x': -3.435593843460083, 'y': -11.100461959838867, 'z': 0.13864082098007202, 'a': -0.0001053236992447637, 'b': -0.003075448563322425, 'g': -0.009757093153893948}]
