import cv2
import numpy as np


def get_roi(image, display=False, set_display_time = -1):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), None)
    retval, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print(f"Threshold value to separate foreground and background is {retval} ")
    eroded_thresh = cv2.erode(thresh, (3, 3), iterations=3)
    contours_image = image.copy()
    cnts, hirerchey = cv2.findContours(eroded_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    biggest_contour = max(cnts, key=cv2.contourArea)
    biggest_contour_area = cv2.contourArea(biggest_contour)
    print(biggest_contour_area)
    if biggest_contour_area > 1000:
        cv2.drawContours(contours_image, [biggest_contour], 0, (0, 0, 255), 2)

    contours_image = image.copy()
    perimeter = cv2.arcLength(biggest_contour, True)
    approx_contour = cv2.approxPolyDP(biggest_contour, perimeter * 0.03, True)
    cv2.drawContours(contours_image, [approx_contour], -1, (0, 0, 255), 2)
    x, y, w, h = cv2.boundingRect(approx_contour)
    cv2.rectangle(contours_image, (x, y), (x + w, y + h), (255, 0, 0), 5)
    # Creating ROI
    roi_mask = np.zeros((image.shape[0], image.shape[1]), dtype="uint8")
    cv2.rectangle(roi_mask, (x, y), (x + w, y + h), (255, 255, 255), -1)
    # Extracting ROI
    ROI_image = cv2.bitwise_and(image, image, mask=roi_mask)

    if display :
        cv2.imshow("Gray Image", gray)
        cv2.waitKey(set_display_time)
        cv2.imshow("Blurred Image", blurred)
        cv2.waitKey(set_display_time)
        cv2.imshow("threshold image", thresh)
        cv2.waitKey(set_display_time)
        cv2.imshow("Eroded Image", eroded_thresh)
        cv2.waitKey(set_display_time)
        cv2.imshow("Contours in Image", contours_image)
        cv2.waitKey(set_display_time)
        cv2.imshow("Approximated Polygon from contour", contours_image)
        cv2.waitKey(set_display_time)
        cv2.imshow("Bounding box over ROI", contours_image)
        cv2.waitKey(set_display_time)
        cv2.imshow("ROI for input image", roi_mask)
        cv2.waitKey(set_display_time)
        cv2.imshow("ROI Extracted from image", ROI_image)
        cv2.waitKey(set_display_time)

    return ROI_image


if __name__ == "__main__" :
    print("Counting Eggs")

    set_display_time = -1

    image = cv2.imread("./images/eggs_5_top_view.jpeg")
    cv2.imshow("Input Image", image)
    cv2.waitKey(set_display_time)

    roi = get_roi(image)
    cv2.imshow("ROI", roi)
    cv2.waitKey(set_display_time)



