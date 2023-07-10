import cv2
from detect_tshirt import employee_finder


if __name__ == "__main__" :
    print("Finding Employees")
    # image = cv2.imread("./images/green_tshirt4.jpg")
    # image = employee_finder(image)
    # cv2.imshow("output", image)
    # cv2.waitKey(1)

    # Running algorithm on video

    video = cv2.VideoCapture("./images/green_tshirt_on_floor.mov")

    while True:
        ret, frame = video.read()
        if not ret:
            print("video_ended")
            break

        frame = employee_finder(frame)
        cv2.imshow("looking for employees", frame)
        cv2.waitKey(1)