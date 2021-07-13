#Name- Pratishtha
#Code for- To convert all images saved in a directory to Grayscale

pip install opencv-python

import cv2

import os,glob

from os import listdir,makedirs

from os.path import isfile,join
path = 'D:/OneDrive/Desktop/v7' # Source Folder
dstpath = 'D:/OneDrive/Desktop/gs7' # Destination Folder
try:
    makedirs(dstpath)# in case, the destination folder aka directory is not present, it will be created
except:
    print ("Directory already exist, images will be written in same folder")
    
files = list(filter(lambda f: isfile(join(path,f)), listdir(path))) #for all files in the directory
for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,gray)
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil) 
        gray_image = cv2.cvtColor(os.path.join(path,image), cv2.COLOR_BGR2GRAY) # convert to grayscale
        cv2.imwrite(os.path.join(dstpath,fil),gray_image)
    except:
        print('{} is not converted')
