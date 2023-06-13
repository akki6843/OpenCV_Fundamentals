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

    # Applying Adaptive Threshold on blurred image

    binary_image = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 1)
    cv2.imshow("Adaptive Threshold", binary_image)
    cv2.waitKey(-1)
