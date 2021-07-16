## Solution to Issue#24 - NO_PAIN [vid 37-39]  

**GOAL**  
Extract 50 rgb images from each of the videos assigned and classify them into 3 folders based on expression (Mild-No pain, Moderate pain, Severe pain) which will be stored in the Image Datasets folder. These images should also be converted into grayscale and classified into the correct folders.  

**PURPOSE**  
The purpose of this issue is to help with the creation of the dataset using which the model is going to be trained.     

**DATASET**  
The data used for this issue are videos 37-39 in the Nopain folder from the [iCOPEvid OneDrive link](https://livemissouristate-my.sharepoint.com/:f:/g/personal/nyc10040_missouristate_edu/Ev2GCLuXRK1DsgbeiRGRywkBBzLLqRH-OKaMi3rFHuM3iA?e=Zm3XcU).  

**DESCRIPTION**   
The basic approach to this issue would be to take each video file, then read only the required frames by skipping over the other frames such that only 50 (equally spaced) frames are read from each file. Once each frame is read it can be converted to grayscale and saved. This can then be repeated for all the video files.  

**WHAT I HAD DONE**    
1. The required videos are downloaded and stored in the videos folder which can be found in the model folder along with the code(Extract Frames.ipynb). 
2. To extract the images first a VideoCapture object is created. 
3. In order to extract 50 frames first get the total no. of frames and then divide by 50 to get the step value, which is how many frames to skip before reading the next frame. 
4. Then iterate from i=0 to i=49, each time setting the next frame to be read as *i x step*, to read the required frames. 
5. These images are then converted to grayscale using cv2.cvtColor() and both versions are saved in the save directory. 
6. This process is repeated for all the videos stored in the video folder by using glob.glob() which can get all the files matching the specified pattern. 
7. The images are then manually classified into the 3 folders based on expression (Mild-No pain, Moderate pain, Severe pain).
  
**WORKFLOW OF PROJECT FILES**  
Workflow of script:  
1. Get the path for all the video files and iterate for each video file.
2. Read the video file calculate step value from total no. of frames. 
3. Iterate 50 times, read the required frames, convert to grayscale and save both versions  
  
Once the image files are saved, they are classified into the appropriate folder.

  
**STATE YOUR PROCEDURE AND UNDERSTANDING FROM YOUR WORK**  
The first step was to research different methods for extracting frames from a video file and by far the most popular method was to create a VideoCapture object and use the read() method. The next step was to find a way to extract a specific number of equally spaced frames. Upon redaing further about the VideoCapture class, I found out about VideoCaptureProperties which has several useful properties such as the total number of frames as well as the position in frames. Also it is possible to set values for these properties. One approach that I found, utilises these properties to get a step value and skips frames while reading so as to get the required number of frames spaced out throughout the video and this approach seemed to work quite well. After getting this to work with a single video all that had to be done was to use glob to get the paths to all the video files in one variable and iterate for all the videos. To convert the images to grayscale and to save the images I found the cvtColor() and imwrite() functions respectively. The references that I used have been given under References.        
  
**DETAILED EXPLANATION OF SCRIPT, IF APPLICABLE**  
Refer to the script file which is in the form of a Python Notebook which is well commented and explains the code clearly.
  

**Libraries needed**  
1. cv2
2. glob
  
**COMPILATION STEPS**  
1. Import Libraries.
2. Get video file paths and iterate.
3. Read each video and iterate 50 times.
    * Set next frame using step value  
    * Extract frame  
    * Convert to grayscale    
    * Save both versions  
    
  
**RESEARCH**  
As a beginner in OpenCV, I had to research the different ways to extract frames from videos and then the different methods and properties of the VideoCapture class so that I could extract the frames in the way that was required for the issue. The different sources that I used have been mentioned below under References.  
  
**CONCLUSION**  
I was able to extract 100 images (50 RGB and 50 grayscale) for each of the 3 assigned videos successfully and then classify them into the appropriate folders. This being my first experience with openCV, I am very happy to complete the task and learn several new concepts along the way. 
  
**REFERENCES**  
1. [Extracting approach](https://stackoverflow.com/questions/54705500/python-extract-n-frames-in-different-length-of-video)
2. [Understanding the VideoCapture class](https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html)
3. [Using glob](https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/)
  
**Author**  
Sumant Binil  
GitHub id:- [Sumantbinil](https://github.com/Sumantbinil)  
[Connect on LinkedIn](https://www.linkedin.com/in/sumant-binil-142913174/)
