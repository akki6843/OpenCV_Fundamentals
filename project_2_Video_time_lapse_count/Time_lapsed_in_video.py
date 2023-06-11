import cv2
from datetime import datetime as dt

if __name__ == "__main__":
    # VideoFile Location
    videoFileLocation = "OpenCV_Fundamentals/project_2_Video_time_lapse_count/videos/video.mp4"
    startTime = dt.now()
    # Reading Video file
    video = cv2.VideoCapture(videoFileLocation)

    # Getting video attributes
    video_fps = video.get(cv2.CAP_PROP_FPS)
    video_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)

    # Preparing Video Writer to record and save manipulated video
    forcc = cv2.VideoWriter_fourcc(*'MP4V')
    savepath = "OpenCV_Fundamentals/project_2_Video_time_lapse_count/videos/recorded_video.mp4"

    writer = cv2.VideoWriter(savepath, forcc, int(
        video_fps), (int(video_width), int(video_height)), True)

    # Video Processing block
    while True:
        grabbed, frame = video.read()
        deltaTime = (dt.now() - startTime).total_seconds()
        if grabbed == False:
            print("No frame captured, Video ended !!!")
            cv2.waitKey(1000)
            break
        else:
            # frame = apply something on frame to manipulate
            # making video gray
            message = str(deltaTime) + " seconds elapsed"
            cv2.putText(img=frame, text=message,
                        org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                        fontScale=1, color=[0, 255, 0])
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Output", frame)
            cv2.waitKey(50)
            writer.write(frame)
