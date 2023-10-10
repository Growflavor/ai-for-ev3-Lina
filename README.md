# ai-for-ev3
A Robot that classifies letters

folder <b>test</b> contains code for classifying the selected file, the trained model and some files that where read to be classified

files <b>data_XX_XX_XX.XXXXXX</b> are the files that are written from the robot when <b>line.py</b> is executed

<b>line.py</b> is run by ev3 to follow a line and write necessary data to a file

<b>letter_classifier.py</b> is run by ev3 and is the same as <b>line.py</b> plus the classification of the letter that is read and the "announcement" of the result

<b>read_arrays.py</b> is run on the computer and trains the model with the files <b>data_XX_XX_XX.XXXXXX</b>
