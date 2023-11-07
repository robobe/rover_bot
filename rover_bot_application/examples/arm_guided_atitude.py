import time
import sys
from math import radians
from pymavlink import mavutil

master = mavutil.mavlink_connection('udp:0.0.0.0:14550')

# Make sure the connection is valid
master.wait_heartbeat()

mode = 'GUIDED'

# Check if mode is available
if mode not in master.mode_mapping():
    print('Unknown mode : {}'.format(mode))
    print('Try:', list(master.mode_mapping().keys()))
    sys.exit(1)

mode_id = master.mode_mapping()[mode]

master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    mode_id)

# Get some information !
while True:
    try:
        ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
        ack_msg = ack_msg.to_dict()
        # https://mavlink.io/en/messages/common.html#SET_MODE
        if ack_msg['command'] == 11:
            break
    except:
        pass
    time.sleep(0.1)


# Arm
# master.arducopter_arm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')


thrust = 1
att_target = [0, 0, 0, 0]
master.mav.set_attitude_target_send(
    0,  # system time in milliseconds
    master.target_system,
    master.target_component,
    7,         # type mask
    att_target,   # quaternion attitude
    radians(0),    # body roll rate
    radians(0),   # body pitch rate
    radians(0),     # body yaw rate
    thrust)       # thrust