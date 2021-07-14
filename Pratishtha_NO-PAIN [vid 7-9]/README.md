**Extracting 50 RGB images of the baby's facial expressions from each video. Later, convert the 50 RGB images to gray scale images. So, you will be extracting totally 100 images from each video. You have been assigned with 3 videos i.e., video [7-9] in the dataset present under 'Nopain' folder which contains 126 videos.**

**GOAL**

To extract a total of 100 images i.e. 50 colored and 50 grayscale images from vid[7-9] and classify them into 3 folders(no-mild pain, moderate pain, severe pain), based on the facial expression of the newborn.


**PURPOSE**

My purpose was not only to achieve the mentioned goal, but also to learn along, and so I did my research on how to use OpenCV technique to extract images and then, implemented it in my code, then further worked on my code to make it better, and increase the time efficiency to be able to work on multiple files at the same time and extracted the images and classified them.


**DATASET**

[Dataset-Video Files](https://livemissouristate-my.sharepoint.com/:f:/g/personal/nyc10040_missouristate_edu/Ev2GCLuXRK1DsgbeiRGRywkBBzLLqRH-OKaMi3rFHuM3iA?e=Zm3XcU)


**DESCRIPTION**

I read about How to extract images from multiple sources, you may refer to the references below and then implemented it in my code, to extract 50 images of both the types( colored as well as grayscale) for all 3 videos that I was assigned with.


**WHAT I HAD DONE**

First, you can refer my code files in Model folder to understand the code I have used(which is commented to make it easy to understand), then to see the Outcome of my approach, refer to Image Datasets folder and you can see the Colored and Grayscale images in different respective folders. My approach was to simply learn about how to use cv2 and other libraries for extracting image frames and then work on it.


**WORKFLOW OF YOUR PROJECT FILES**

Refer to compilation steps below, and go through the code. The final Image Datasets folder has images classified into folders based on Facial Expressions. My workflow has been - Learn, Code, Extract, Save images , and then convert those to grayscale and save those, and finally classify the images into different folders.


**STATE YOUR PROCEDURE AND UNDERSTANDING FROM YOUR WORK**

I did discuss the problem and how to approach the issue with Project Admin, who gave good reference to look through and with their guidance, I read from sources and implemented learnt knowledge into my code to make it better, simpler and to save time too, and finally come up with the Image Datasets folder.


**DETAILED EXPLANATION OF SCRIPT, IF APPLICABLE**

My code files are added with comments to undrstand my approach.


**LIBRARIES NEEDED**

- cv2
- os
- Glob

**COMPILATION STEPS**

Import Libraries   
->Read the video files from the folder they are saved in    
-> Extract image frames for each video    
-> Save them in a folder    
-> Then, convert these frames to grayscale    
-> Save them in a folder.


**RESEARCH**

I was completely new to OpenCV, so this was an exposure opportunity, where I got to learn about how to extract images, I have added references below of the sources that I have learnt from and hopefully I will be able to extract any image frames from now onwards.


**SCREENSHOTS**

The images in the Image Dataset folder are the Output of my code.


**CONCLUSION**

The conclusion is after researching and implementing into my Code and then, classifying Images, the Dataset will be used to come up with a model to save lives of many newborn babies which are at a very high-risk, especially the ones that are born before 9 months of pregnancy (also called as Preterm babies).




**REFERENCES**

[Reference 1](https://theailearner.com/2018/10/15/extracting-and-saving-video-frames-using-opencv-python/)

[Reference 2](https://medium.com/nerd-for-tech/extraction-of-frames-from-multiple-videos-3ddbced6f3c2)

[Reference 3](https://techtutorialsx.com/2018/06/02/python-opencv-converting-an-image-to-gray-scale/)

**NAME OF AUTHOR**

## ***Pratishtha***

[Connect with me on LinkedIn](https://www.linkedin.com/in/pratishtha-s-a0a812203)


