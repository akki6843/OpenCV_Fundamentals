import cv2
import numpy as np

if __name__ == "__main__":
    print("Accessing Video directly from a webcam")
    
     # Reading Video file
    video = cv2.VideoCapture(0)
    
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
            cv2.waitKey(1) 