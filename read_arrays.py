import pandas as pd
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle


def pad_arrays(array, longest):
    if len(array) < longest:
        filler = longest - len(array)
        filler_array = []
        for i in range(0, filler):
            zero_array = [0, 0, 0, 0]
            filler_array.append(zero_array)

        return np.concatenate((array, filler_array), axis=0)
    else:
        return array


movements = []
col_names = ['left', 'right', 'motor_left', 'motor_right']

directory = os.getcwd()
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        data = pd.read_csv(filename, names=col_names, header=None)
        movement = data.values
        movements.append(movement)

longest_array = len(max(movements, key=len))
new_movements = []

for i in movements:
    new_movements.append(pad_arrays(i, longest_array))


new_new_movements = []

for i in new_movements:
    condensed_movement = []
    for n in range(0, 4):
        counter = 1
        new_value = 0
        for j in i:
            new_value += j[n]
            counter += 1
        new_value = new_value / counter
        condensed_movement.append(new_value)
    new_new_movements.append(condensed_movement)

driven_number = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

data_movement = pd.DataFrame(new_new_movements)

X = data_movement
y = driven_number

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 3)
# Fit the classifier to the data
knn.fit(X_train,y_train)

#show predictions on the test data
print(knn.predict(X_test))

#check accuracy of our model on the test data
print(knn.score(X_test, y_test))
# sv_classifier = SVC(kernel='rbf') 65% acc
# sv_classifier = SVC(kernel='poly', degree=8) 85% acc

file = 'trained_model.sav'
pickle.dump(knn, open(file, 'wb'))

