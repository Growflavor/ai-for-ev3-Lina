#!/usr/bin/env python3

"""
This line follower can be used to classify digits
To collect train and test data, use the counterpart line follower
This is the better line following algorithm, but:
The trained models and the train and test data in the data folder were collected with the v1 line follower
Therefore, when working with this classifier, it's best to collect your own data with the counterpart line follower v2
"""

#Line follower code here

from ev3dev.auto import *
import pickle


def run():
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
    
    col_left = col_left / 557
    col_right = col_right / 557
    left_motor= left_motor / 557
    right_motor = right_motor / 557

    X_new = [[col_left, col_right, left_motor, right_motor]]

    print(str(col_left) + " " + str(col_right) + " " + str(left_motor) + " " + str(right_motor))

    # Load model and scaler
    loaded_model = pickle.load(open("trained_model.sav", 'rb'))

    # Classify new data
    y_new = loaded_model.predict(X_new)
    letters = ["C","J"]
    print (letters[y_new[0]])
    Sound.speak(letters[y_new[0]])

run()