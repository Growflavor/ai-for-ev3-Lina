#!/usr/bin/env python3

"""
This line follower can be used to classify digits
To collect train and test data, use the counterpart line follower
This is the better line following algorithm, but:
The trained models and the train and test data in the data folder were collected with the v1 line follower
Therefore, when working with this classifier, it's best to collect your own data with the counterpart line follower v2
"""

#Line follower code here

def classify():
    
    left_sensor = left_sensor / 557
    mid_sensor = mid_sensor / 557
    right_sensor = right_sensor / 557
    left_motor_count = left_motor_count / 557
    right_motor_count = right_motor_count / 557

    X_new = [[left_sensor, right_sensor, left_motor_count, right_motor_count]]

    print(str(left_sensor) + " " + str(right_sensor) + " " + str(left_motor_count) + " " + str(right_motor_count))

    # Load model and scaler
    loaded_model = pickle.load(open("""file path""", 'rb'))
    loaded_scaler = pickle.load(open("""file path""", 'rb'))

    # Apply scaler
    X_new = loaded_scaler.transform(X_new)

    # Classify new data
    y_new = loaded_model.predict(X_new)
    letters = ["C","J"]
    print letters[y_new[0]]
    Sound.speak(letters[y_new[0]])

run()
classify()