#!/usr/bin/env python3

"""
This line follower can be used to collect test data
To classify digits or shapes, you can use the classifier counterpart that classifies based on a trained imported model
This is the better line following algorithm, but:
The trained models and the train and test data in the data folder were collected with the v1 line follower
Therefore, when working with this line follower, it's best to collect your own data with this script
"""
# Import the EV3-robot library
from ev3dev.auto import *
import datetime
# Connect motors
left_motor = LargeMotor(OUTPUT_B)
assert left_motor.connected
right_motor = LargeMotor(OUTPUT_C)
assert right_motor.connected

# Connect touch sensor and color sensors
ts = TouchSensor()
assert ts.connected
col_left = ColorSensor('in1')
assert col_left.connected
col_right = ColorSensor('in4')
assert col_right.connected

# Change color sensor mode
col_left.mode = 'COL-REFLECT'
col_right.mode = 'COL-REFLECT'


def run():
    left = []
    right = []
    thresh = 55
    while not ts.value():
        # Add sensor values to respective list
        left.append(col_left.value())
        right.append(col_right.value())

        if left[-1] > thresh and right[-1] > thresh:
            right_motor.run_forever(speed_sp=90)
            left_motor.run_forever(speed_sp=90)
        if left[-1] < thresh:
            left_motor.run_forever(speed_sp=0)
            right_motor.run_forever(speed_sp=100)
        if right[-1] < thresh:
            right_motor.run_forever(speed_sp=0)
            left_motor.run_forever(speed_sp=100)
        

        # Write sensor data to text file
        f.write(str(col_left.value()) + "," + str(col_right.value()) + "," + str(
            left_motor.speed) + "," + str(right_motor.speed) + "\n")

fname = "data_" + str(datetime.datetime.now().time()) + ".txt"
f = open(fname, "w+")
run()
left_motor.stop()
right_motor.stop()
f.close()
