# AI-ML-for-Newborn-Babies-in-Healthcare

**GOAL**

The goal of this is to extract 50RGB images from the video given and then convert these RGB into grayscale.It means extract total 100 images from videos.After extracting images,classify them as per newborn baby facial expression as No Mild Pain, Moderate Pain and Severe pain.


**PURPOSE**

Purpose of this issue is to explore the Opencv as here in this I learn to extract images and explore Opencv library and implement these things in my code and further improved my code to make it efficient and less complex,so that it is able to to work on multiple files containing videos and extract images efficiently.


**DATASET**

[Dataset-Video Files](https://livemissouristate-my.sharepoint.com/:f:/g/personal/nyc10040_missouristate_edu/Ev2GCLuXRK1DsgbeiRGRywkBBzLLqRH-OKaMi3rFHuM3iA?e=Zm3XcU)
Password :- 3maF'N+53xKj{


**DESCRIPTION**

In this project I used Opencv module to extract images and iterate over multiple file records using Os module and extracted images.Do read below information for get description of what I had done.


**WHAT I HAD DONE**

- Firstly, Imported required modules for extracting and iterating over image i.e Opencv(cv2) and Os module.
- After importing modules, I iterate over the folder which contain the video files assigned to me.
- Then,I loop over the video to calculate the total frames.
- After that I read videoo frame by frame and then to exactly extract 50 rgb images I used modulus operation(i%12) to save frames multiple of 12.
- After saving 1 rgb image then I convert this rgb frame into grayscale format.
- In this way I extract 100 images from each videos and saved them in folder.
- After extracting total 200 images from 2 videos , I manually classified images as per the facial expression of newborn baby in three categories(No Mild Pain, Moderate, Severe Pain).
- Finally the work is completed successfully.


**WORKFLOW OF YOUR PROJECT FILES**

Refer the above section in which I mentioned all the steps that I had taken and you can also refer to comment that I had written in Jupyter notebook which will be helpful for uunderstanding each line of code

**STATE YOUR PROCEDURE AND UNDERSTANDING FROM YOUR WORK**

I had a discussion with Project Admin who gave me overall concept behind this project. I had prior knowledge of Opencv but now I learned how to implement it in real world scenario.I choose this methodology because it is easier to implement and less complex.


**DETAILED EXPLANATION OF SCRIPT, IF APPLICABLE**

I gave the detailed explanation in all the above mentioned points.


**LIBRARIES NEEDED**

- Opencv (cv2)
- OS


**COMPILATION STEPS**


Import Libraries   
->Read the video files from the folder.   
-> Extract video frame by frame    
-> Saved rgb images    
-> Convert the rgb frame images to grayscale.   
-> Save them in a folder.


**RESEARCH**

I had prior knowledge of Opencv ,so for this issue I didn't research that much.


**SCREENSHOTS**

The images in the Image Dataset folder are the Output of my code.


**CONCLUSION**

The conclusion is that after implementing this code and extracting images and classifying them, now the dataset is ready to get trained  and for saving the life of newborn babies.


<!--**REFERENCES**

Add all the references you had gone through to make your PR successful.-->


**NAME OF AUTHOR**

### Arihant Rode 
- Github :- [@arihantrode89](https://github.com/arihantrode89)
- [Connect with me on LinkedIn](https://www.linkedin.com/in/pratishtha-s-a0a812203)

<!--**DISCLAIMER, IF ANY**

Use this section to mention if any particular disclaimer is -->


