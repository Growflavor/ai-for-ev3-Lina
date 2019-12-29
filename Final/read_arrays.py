import pandas as pd
import numpy as np
import os
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
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

# Create KNN classifier
knn_cv = KNeighborsClassifier(n_neighbors=3)  # 97.5% !!!!
# Fit the classifier to the data
# train model with cv of 10
# sv_classifier = SVC(kernel='rbf') 65% acc
# sv_classifier = SVC(kernel='poly', degree=8) 85% acc
cv_scores = cross_val_score(knn_cv, X, y, cv=10)
# print each cv score (accuracy) and average them
file = 'trained_model.sav'
pickle.dump(knn_cv, open(file, 'wb'))
print(cv_scores)
print('cv_scores mean:{}'.format(np.mean(cv_scores)))
