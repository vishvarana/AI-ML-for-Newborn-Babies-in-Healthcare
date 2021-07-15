# Importing all necessary libraries
import cv2
import glob
import os

try:
    # creating a folder named GrayScale_Images
    if not os.path.exists('35a'):
        os.mkdir('./Image Dataset/svaed images/35a')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of 35a')

images_path = glob.glob('./Image Dataset/svaed images/35a/*.jpg')

i = 0
for image in images_path:
    img = cv2.imread(image)
    gray_images = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Images', gray_images)

    # writing the extracted images
    cv2.imwrite('./Image Dataset/svaed images/35a/image%02i.jpg' %i, gray_images)

    # increasing counter so that it will
    # show how many frames are created
    i += 1

    # Release all space and windows once done
    cv2.waitKey(600)
    cv2.destroyAllWindows()