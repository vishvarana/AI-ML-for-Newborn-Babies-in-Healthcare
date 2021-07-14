#NAME-Pratishtha
#This is my code to extract image frames from Multiple Videos to avoid having to run code for every video separately
import cv2
import os
no_pain_videos=glob.glob('D:/OneDrive/Desktop/aibabies') # I have passed the source folder where the videos(whose frames are to be extracted) are present
np_video_list=[]#I have created an empty list to store the source videos 
for video in no_pain_videos: #This for loop is to iterate over videos in folder
    for v in glob.glob(video+'/*.mp4'): # to make sure that videos with mp4 extension are being iterated
        np_video_list.append(v) #I have add the videos with mp4 extension, using append
i=1
for j in range(0,len(np_video_list)): #To iterate over the videos added to the list
    video_data=np_video_list[j]
    cap=cv2.VideoCapture(video_data) #To open the video file
    while cap.isOpened():
        ret,frame=cap.read()
        if ret:
            i = i + 1
            if i % 12 == 0:
                name = 'D:/OneDrive/Desktop/raw/v8' + '/' +'NO_PAIN_vid8_'+ str(i) + '.jpg' #name and location of frames to be saved, one can declare location outside too
                cv2.imwrite(name, frame)
                    
                print('Creating ' + name)
        else:
            break
    cap.release()
