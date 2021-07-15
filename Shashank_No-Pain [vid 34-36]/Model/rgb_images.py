# Importing all necessary libraries
import cv2
import os

try:
    # creating a folder named GrayScale_Images
    if not os.path.exists('35a'):
        os.mkdir('.Image Dataset/svaed images/35a')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of 35a')

# Opens the Video file
cap = cv2.VideoCapture('./ICOPEvid/iCOPEvid/Nopain/S010_Friction_1_[0]_20s.mp4')
try:
    # creating a folder named Image datasets
    if not os.path.exists('./Image Dataset/svaed images/35a'):
        os.makedirs('./Image Dataset/svaed images/35a')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# increasing counter so that it will
# show how many frames are created
i = 1

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        i = i + 1
        if i % 12 == 0:
            name = './Image Dataset/svaed images/35a' + '/' + str(i) + '.jpg'
            cv2.imwrite(name, frame)
            print('Creating...' + name)
    else:
        break

# Release all space and windows once done
cap.release()
