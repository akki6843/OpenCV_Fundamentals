import cv2


if __name__ == "__main__":

    # Reading and displaying input Image
    img = cv2.imread(
        "OpenCV_Fundamentals/project_3_Counting_number_of_candies_on_desk/images/many_m_n_m.jpg")
    cv2.imshow("Input", img)
    cv2.waitKey(-1)

    # Converting input image to greyscale image

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grey", grey)
    cv2.waitKey(-1)

    # Applying Gaussian Blur on grey Image

    blurred = cv2.GaussianBlur(grey, (15, 15), None)
    cv2.imshow("Blurred", blurred)
    cv2.waitKey(-1)

    # Applying Threshold to blurred image to make a binary image
    # Here the threshold has been added as a hardcoded value after some trial and error
    retVal, binary_image = cv2.threshold(
        blurred, 230, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("binary image", binary_image)
    cv2.waitKey(-1)
