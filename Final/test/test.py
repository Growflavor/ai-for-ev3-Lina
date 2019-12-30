import pickle
filename = 'trained_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
filename = input('Enter the name of file:')
left_sens = 0
right_sens = 0
left_motor = 0
right_motor = 0
with open(filename) as file:
    for line in file:
        line = line.strip('\n')
        split = line.split(',')
        left_sens = left_sens + int(split[0])
        right_sens = right_sens + int(split[1])
        left_motor = left_motor+ int(split[2])
        right_motor = right_motor + int(split[3])

left_sens = left_sens / 557
right_sens = right_sens / 557
left_motor = left_motor / 557
right_motor = right_motor / 557

X_new = [[left_sens, right_sens, left_motor, right_motor]]

y_new  = loaded_model.predict(X_new)

print(y_new)
