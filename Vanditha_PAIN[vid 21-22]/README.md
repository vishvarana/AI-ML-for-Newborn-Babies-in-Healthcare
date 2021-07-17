PROJECT TITLE 

AI-ML-for-Newborn-Babies-in-Healthcare



ISSUE 

PAIN [vid 21-22] #25



GOAL 

The goal of the project to develop a Machine Learning algorithm for classifying the facial expressions of Newborn babies in the Hospital as per the Pain Scale Assessment on a scale of 10.



PURPOSE

The purpose of this issue was to extract 50 images each from both videos and convert them to grayscale images. Later, classify those images into 3 categories namely No-Mild, Moderate and Severe based on the facial expressions of the babies.



DATASET

 Videos 21-22 from Pain folder in  [DATASET](https://livemissouristate-my.sharepoint.com/:f:/g/personal/nyc10040_missouristate_edu/Ev2GCLuXRK1DsgbeiRGRywkBBzLLqRH-OKaMi3rFHuM3iA?e=Zm3XcU)



PROCEDURE

I have downloaded the required dataset from the link in ZIP format. Later, stored those videos in the Dataset folder on my local machine.

Written the code to extract 50 images from each video.


LIBRARIES REQUIRED 

*cv2

*os

Compilation steps:

  -> Read videos one by one from the folder where they are stored. I have used os module for this purpose.
  
  -> Extract images from each video.
  
  -> Save the images in specific folder.
  
  -> Convert the images into grayscale.
  
  -> Save the gray images in specific folder.

Classified total 200 images into 3 different folders based on the expressions.


UNDERSTANDINGS FROM THE WORK

Got a clear understanding on how to use os module to get to different folders.

There are different ways to approach this solution. But thought of implementing the solution using opencv module.

Learnt how to capture different frames from a video using cv2.VideoCapture(). 

Learnt how to save the extracted images using cv2.imwrite().

To convert BGR image to Grayscale, I have used cv2.cvtColor( _ , cv2.COLOR_BGR2GRAY).



RESEARCH

I had no idea about this condition of newborn babies. So have done some research on that. I observed the facial expressions carefully especially the eyes before classifying the images.

I also have done some research on other techniques to deal with images, later came up with idea to use opencv.


CONCLUSION

I have extracted 200 images from 2 videos and classified them into 3 folders as per the expressions.

This dataset can be used to train the model which can predict the risk of survival of the Preterm newborn babies through Pain-Scale Assessment technique.

The output of this work is in Image Dataset folder.


SCREENSHOTS

No-Mild Pain

![S021_Pain_34](https://user-images.githubusercontent.com/65328075/126023420-45f8afde-654c-40fa-9142-d5f643fbc13c.jpg)


Moderate Pain

![S021_Pain_24](https://user-images.githubusercontent.com/65328075/126023440-8f65b167-af4a-4478-b90c-d35610833ecd.jpg)


Severe Pain 

![S021_Pain_2](https://user-images.githubusercontent.com/65328075/126023465-6728b1d1-be1b-4609-a461-235041c8dacf.jpg)




REFERENCES

[Reference 1](https://theailearner.com/2018/10/15/extracting-and-saving-video-frames-using-opencv-python/)

[Reference 2](https://www.geeksforgeeks.org/extract-images-from-video-in-python/)



NAME OF AUTHOR

Vanditha M

Connect with me on [LinkedIn](https://www.linkedin.com/in/vanditha07/)
