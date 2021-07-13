pip install opencv-python

import cv2
import os
# Opens the Video file
cap = cv2.VideoCapture('D:/OneDrive/Desktop/vids/no_pain/S003_Friction_1_[0]_20s.mp4')
try:
    # creating a folder to save images
    if not os.path.exists('D:/OneDrive/Desktop/raw/v8'):
        os.makedirs('D:/OneDrive/Desktop/raw/v8')
# if not created then raise error
except OSError:
    print('Error: Creating directory of data')
i = 1
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        i = i + 1
        if i % 12 == 0:
            name = 'D:/OneDrive/Desktop/raw/v8' + '/' +'NO_PAIN_vid8_'+ str(i) + '.jpg'
            cv2.imwrite(name, frame)
            print('Creating...' + name)
    else:
        break
cap.release()
