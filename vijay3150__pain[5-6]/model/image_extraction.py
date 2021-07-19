import os
import os.path
import cv2

# directory where data is present
os.chdir(r"C:\Users\vijay.N\Desktop\Classification\Dataset")
# directory to store the frames
save_dir = r"C:\Users\vijay.N\Desktop\Classification\frames"

for element in os.listdir(os.getcwd()):
    vid_path = os.path.join(os.getcwd(), element)

    cap = cv2.VideoCapture(vid_path)
    i = 1
    count = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if i%11 == 0:
            count += 1
            # saving the color image
            cv2.imwrite(os.path.join(save_dir, (element[0:10] + str(count) + '.jpg')), frame)

            # convert the image into grayscale
            grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # saving the grayscale image
            cv2.imwrite(os.path.join(save_dir, (element[0:10] + "gray" + str(count) + '.jpg')), grayImage)
        i+=1

    cap.release()
    cv2.destroyAllWindows()
