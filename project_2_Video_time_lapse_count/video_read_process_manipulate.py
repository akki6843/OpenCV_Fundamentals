# This code is to process a stored video file and perform video processing frame by frame
import cv2
import numpy as np 


if __name__ == "__main__":
    # VideoFile Location 
    videoFileLocation = "OpenCV_Fundamentals/project_2_Video_time_lapse_count/videos/video.mp4" 
    
    # Reading Video file
    video = cv2.VideoCapture(videoFileLocation)
    
    # Video Processing block
    while True :
        grabbed, frame = video.read()
        
        if grabbed == False :
            print("No frame captured, Video ended !!!")
            break
        else :
            # frame = apply something on frame to manipulate
            # making video gray 
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Output", frame)
            cv2.waitKey(-1)  
    