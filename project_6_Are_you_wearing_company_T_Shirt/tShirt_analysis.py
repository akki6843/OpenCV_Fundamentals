import cv2
import numpy as np

if __name__ == "__main__":
    print("Starting T Shirt Analysis")
    image = cv2.imread("./images/IMG_0973.jpeg")
    cv2.imshow("Input", image)
    cv2.waitKey(-1)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (21, 21), None)
    cv2.imshow("Blured Gray", blurred)
    cv2.waitKey(-1)

    retval, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
    print(f"After Calculating OTSU threshold, identified pivot is {retval}")
    cv2.imshow("OTSU Threshold", thresh)
    cv2.waitKey(-1)

    # Performing Morphological Operations

    morphological_mask = np.ones((11, 11))

    thresh = cv2.erode(thresh, morphological_mask, iterations=2)
    cv2.imshow("Eroded Threshold Image ", thresh)
    cv2.waitKey(-1)

    thresh = cv2.dilate(thresh, morphological_mask, iterations=2)
    cv2.imshow("Dilated Threshold Image ", thresh)
    cv2.waitKey(-1)

    # Getting contours

    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(gray, cnts, -1, (0, 0, 255), 5)
    cv2.imshow("Contoured Image", image)
    cv2.waitKey(-1)

    # Creating Mask from the contour

    mask = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')
    cv2.drawContours(mask, cnts, -1, (255, 255, 255), -1)
    cv2.imshow("Mask From Contours", mask)
    cv2.waitKey(-1)

    # Extracting T-shirt from image using mask
    tShirt_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Extracted T-Shirt", tShirt_image)
    cv2.waitKey(-1)