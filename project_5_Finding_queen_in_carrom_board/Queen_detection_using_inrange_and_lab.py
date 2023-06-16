import cv2

# Contours can become inputs for calculating rectangles and circles to draw onm image as BBOXs

if __name__ == "__main__":
    image = cv2.imread(
        "OpenCV_Fundamentals/project_5_Finding_queen_in_carrom_board/images/carrom_board.jpg")
    cv2.imshow("Input", image)
    cv2.waitKey(-1)

    blurred = cv2.GaussianBlur(image, (3, 3), None)

    lab_image = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

    binary_image = cv2.inRange(lab_image, (0, 165, 145), (255, 175, 155))
    cv2.imshow("Binary Image", binary_image)
    cv2.waitKey(-1)

    contours, hierarchy = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, None)

    print(len(contours))
    max_area_contour = max(contours, key=cv2.contourArea)
    max_area = cv2.contourArea(max_area_contour)
    print(max_area_contour, max_area)

    if max_area > 50:
        cv2.drawContours(image, [max_area_contour], 0, (0, 255, 0), -1)
        cv2.putText(image, "Queen Found", (10, 10),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
        cv2.imshow("Detection", image)
        cv2.waitKey(-1)

    else:
        cv2.putText(image, "Queen not Found", (10, 10),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
        cv2.imshow("Detection", image)
        cv2.waitKey(-1)
