import cv2


def employee_finder(image, plot=False):
    set_visual_delay = -1

    if plot:
        cv2.imshow("Input", image)
        cv2.waitKey(set_visual_delay)

    # Converting image to LAB image
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Blurring LAB image
    blurred = cv2.GaussianBlur(lab_image, (5, 5), None)

    # Setting lower and upper bound for color filtering
    # Lower and Upper bounds were identified from tshirt analysis

    lower_bound = (0, 85, 115)
    upper_bound = (255, 115, 135)

    binary = cv2.inRange(blurred, lower_bound, upper_bound)
    if plot:
        cv2.imshow("mask identified", binary)
        cv2.waitKey(set_visual_delay)

    # getting contours

    cnts, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if cnts:
        biggest_contour = max(cnts, key=cv2.contourArea)
        biggest_contour_area = cv2.contourArea(biggest_contour)
    else :
        biggest_contour_area = 0

    if biggest_contour_area > 200:
        print("Employee")
        cv2.putText(image, "Employee Found", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.drawContours(image, [biggest_contour], 0, (0, 0, 255), 3)
    else:
        print("No Employee")
        cv2.putText(image, "No Employee", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if plot:
        cv2.imshow("Output", image)
        cv2.waitKey(set_visual_delay)
    return image


if __name__ == "__main__":
    print("Detecting T-Shirt")
    image = cv2.imread("./images/IMG_0973.jpeg")
    image = employee_finder(image)
    cv2.imshow("output", image)
    cv2.waitKey(-1)

