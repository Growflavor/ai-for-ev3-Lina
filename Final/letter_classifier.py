#!/usr/bin/env python3

"""
This line follower can be used to classify digits
To collect train and test data, use the counterpart line follower
This is the better line following algorithm, but:
The trained models and the train and test data in the data folder were collected with the v1 line follower
Therefore, when working with this classifier, it's best to collect your own data with the counterpart line follower v2
"""
from ev3dev.auto import *
import pickle
from sklearn.neighbors import KNeighborsClassifier
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
    left_sensor = 0
    right_sensor = 0
    left_motor_count = 0
    right_motor_count = 0
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
        
        left_sensor += col_left.value()
        right_sensor += col_right.value()
        left_motor_count += left_motor.speed
        right_motor_count += right_motor.speed
        
    left_motor.stop()
    right_motor.stop()    
        
        
    left_sensor = left_sensor / 557
    right_sensor = right_sensor / 557
    left_motor_count = left_motor_count / 557
    right_motor_count = right_motor_count / 557

    X_new = [[left_sensor, right_sensor, left_motor_count, right_motor_count]]

    print(str(left_sensor) + " " + str(right_sensor) + " " + str(left_motor_count) + " " + str(right_motor_count))

    # Load model and scaler
    loaded_model = pickle.load(open('trained_model.sav', 'rb'))

    # Classify new data
    y_new = loaded_model.predict(X_new)
    letters = ["C","J"]
    print (letters[y_new[0]])
    Sound.speak(letters[y_new[0]])

run()