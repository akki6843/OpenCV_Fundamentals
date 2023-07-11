import cv2
import numpy as np

from extracting_ROI import get_roi

if __name__ == "__main__":
    print("Processing Roi")
    set_display_time = 100

    image = cv2.imread("images/eggs_2_with_1_outside.jpeg")
    cv2.imshow("Input Image", image)
    cv2.waitKey(set_display_time)

    roi = get_roi(image)
    cv2.imshow("ROI", roi)
    cv2.waitKey(set_display_time)

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray_roi, (5,5), None)
    cv2.imshow("blurred", blurred)
    cv2.waitKey(set_display_time)

    retval, thresh = cv2.threshold(blurred, 200,255, cv2.THRESH_BINARY)
    print(retval)
    cv2.imshow("threshold image", thresh)
    cv2.waitKey(set_display_time)

    cnts, hirerchey = cv2.findContours(thresh, cv2.RETR_LIST    , cv2.CHAIN_APPROX_SIMPLE)
    print(f"Total number of original contours identified {len(cnts)}")

    selected_cnts = []

    for idx , contour in enumerate(cnts):
        area = cv2.contourArea(contour)
        if area > 1000:
            selected_cnts.append(contour)

    selected_circle_cnts=[]

    for idx, contour in enumerate(selected_cnts):
        # Getting enclosing circle on contour as our targets are circular in nature
        (x,y),radius = cv2.minEnclosingCircle(contour)
        # calculating areas of contour and area of enclosing circle
        cnt_area = cv2.contourArea(contour)
        circle_area = np.pi * radius*radius
        print(f"Area of contour is {cnt_area} and area of circle is {circle_area}")
        # now when we compare two areas they should be close by to be an egg
        off_percentage = int(((circle_area - cnt_area)/circle_area)*100)
        print(f"The Two areas are off by {off_percentage}%")
        print("------------------------------------------")
        if off_percentage <= 10:
            selected_circle_cnts.append(contour)


    print(f"Total number of contours after circling {len(selected_circle_cnts)} ")
    cv2.drawContours(roi, selected_circle_cnts, -1, (0, 255, 255), 2)
    cv2.imshow("Contours", roi)
    cv2.waitKey(set_display_time)