import cv2

if __name__ == "__main__":
    # Reading and displaying input Image
    img = cv2.imread(
        "OpenCV_Fundamentals/project_3_Counting_number_of_candies_on_desk/images/many_m_n_m.jpg")
    cv2.imshow("Input", img)
    cv2.waitKey(1)

    # Converting input image to greyscale image

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grey", grey)
    cv2.waitKey(1)

    # Applying Gaussian Blur on grey Image

    blurred = cv2.GaussianBlur(grey, (11, 11), None)
    cv2.imshow("Blurred", blurred)
    cv2.waitKey(1)

    # Applying Adaptive Threshold on blurred image

    binary_image = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
    cv2.imshow("Adaptive Threshold", binary_image)
    cv2.waitKey(1)

    # Finding Contours in the binary image

    contours, hierarchy = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_contours = 0
    candy_contours = []

    for idx, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > 1000:
            print(idx, area)
            total_contours += 1
            candy_contours.append(cnt)
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), -1)
            cv2.imshow("Drawn Contours", img)
            cv2.waitKey(500)

    print(f"Total meaningful contours are {total_contours}")

    cv2.putText(img, f"Total number of candies identified : {total_contours}",
                (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
    cv2.imshow("Drawn Contours", img)
    cv2.waitKey(-1)
