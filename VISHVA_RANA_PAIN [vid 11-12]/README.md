Extracting 50 RGB images of the baby's facial expressions from each video. Later, convert the 50 RGB images to gray scale images. So, you will be extracting totally 100 images from each video. You have been assigned with 3 videos i.e., video [11-12] in the pain dataset present.

GOAL

To extract a total of 100 images i.e. 50 colored and 50 grayscale images from vid[11-12] and classify them into 3 folders(no-mild pain, moderate pain, severe pain), based on the facial expression of the newborn.

PURPOSE

My purpose was to achieve the mentioned goal,and also learn while applying, and so I searched throught the internet regarding the use of OpenCV lib to extract images and then, implemented it in my code, and modified it later on to make it better, for it to be able to work on multiple video datasets at the same time and extracted the images and classified them.

DATASET

https://livemissouristate-my.sharepoint.com/:f:/g/personal/nyc10040_missouristate_edu/Ev2GCLuXRK1DsgbeiRGRywkBBzLLqRH-OKaMi3rFHuM3iA?e=Zm3XcU

DESCRIPTION

Twins, triplets, and other multiples often are admitted to the NICU. This is because they tend to be born earlier and smaller than single birth babies. Babies with health conditions such as breathing trouble, heart problems, infections, or birth defects are also cared for in the NICU. Determining the pain by their expressions, we can try to ease their pain. The classification is done based on expressions into 3 differemt categories - no/mild,moderate and severe. This would help th healthcare system to deal, better and faster with problems.

WHAT I HAD DONE

Reference of my code file is in Model folder, to understand the code I have finally worked with, outcome of the approach, is given in Images folder and colored and gray images will be seen in different folders. Approach was simple,to use cv2 and other libraries for extracting image frames.

WORKFLOW OF YOUR PROJECT FILES

Mentioned above point. The Images folder has images classified into folders based on pained expressions. Workflow is as said - Code, Extract, Save images , and then convert those to grayscale and save those, and finally classify the images into different folders.

STATE YOUR PROCEDURE AND UNDERSTANDING FROM YOUR WORK

Procedure is mentioned above,also I asked few of my peers who gave good reference to look through and with their guidance, I read from sources and implemented it into my project to make it better, simpler and to save time too.

DETAILED EXPLANATION OF SCRIPT, IF APPLICABLE

There are folders with classified images to understand the output, and model folder to understand the input code

LIBRARIES NEEDED

cv2
os
Glob

COMPILATION STEPS

Import Libraries
->Read the video files from the folder they are saved in
-> Extract image frames for each video
-> Save them in a folder
-> Then, convert these frames to grayscale
-> Save them in a folder.

RESEARCH

I was completely new to OpenCV, so this was an exposure opportunity, where I got to learn about how to extract images, I have learnt from this project and various sources and I will be able to extract any image frames from now onwards.

SCREENSHOTS

The images in the Images folder are the Output of my code.

CONCLUSION

The conclusion is after researching and implementing into my Code and then, classifying Images, the Dataset will be used to come up with a model to save lives of many newborn babies which are at a very high-risk, especially the ones that are born before 9 months of pregnancy (also called as Preterm babies).

REFERENCES

https://theailearner.com/2018/10/15/extracting-and-saving-video-frames-using-opencv-python/

https://www.geeksforgeeks.org/extract-images-from-video-in-python/

https://www.youtube.com/watch?v=SWGd2hX5p3U

NAME OF AUTHOR

Vishva Rana
https://www.linkedin.com/in/vishva-rana-bb60a1211/
