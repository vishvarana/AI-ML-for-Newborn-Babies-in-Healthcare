Issue

PAIN [vid 21-22] #25


Project

AI-ML-for-Newborn-Babies-in-Healthcare


Dataset

 Videos 21-22 from Pain folder in  [DATASET](https://livemissouristate-my.sharepoint.com/:f:/g/personal/nyc10040_missouristate_edu/Ev2GCLuXRK1DsgbeiRGRywkBBzLLqRH-OKaMi3rFHuM3iA?e=Zm3XcU)



OBJECTIVE

The goal was to extract 50 images each from both videos and convert them to grayscale images. Later, classify those images into 3 categories namely No-Mild, Moderate and Severe based on the facial expression in the images.



PROCEDURE

I have downloaded the required dataset from the link in ZIP format.
Written the code to extract 50 images from each video.

Libraries required - cv2, os

Compilation steps -

  -> Read videos one by one from the folder where they are stored. I have used os module for this purpose.
  
  -> Extract images from each video.
  
  -> Save the images in specific folder.
  
  -> Convert the images into grayscale.
  
  -> Save the gray images in specific folder.

Classified total 200 images into 3 different folders based on the expression.



UNDERSTANDINGS FROM THE WORK

Got a clear understanding on how to use os module to get to different folders.
Learnt how to extract images using opencv and convert them into grayscale.



RESEARCH

I had no idea about this condition of newborn babies. So have done some research on that. I observed the facial expressions carefully especially the eyes before classifying the images.



CONCLUSION

This dataset can be used to train the model which can predict the risk of survival of the Preterm newborn babies through Pain-Scale Assessment technique.
The output of this work is in Image Dataset folder.



REFERENCES

[Reference 1](https://theailearner.com/2018/10/15/extracting-and-saving-video-frames-using-opencv-python/)

[Reference 2](https://www.geeksforgeeks.org/extract-images-from-video-in-python/)



NAME OF AUTHOR

Vanditha M

Connect with me on [LinkedIn](https://www.linkedin.com/in/vanditha07/)
