import cv2

import cv2


def show_image(Name="Window", img=[0, 0, 0], wait=-1):
    cv2.imshow(f"{Name}", img)
    cv2.waitKey(wait)


def preprocess_input_img(img):
    # Converting input image to greyscale image
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applying Gaussian Blur on grey Image
    blurred = cv2.GaussianBlur(grey, (11, 11), None)

    # Applying Adaptive Threshold on blurred image
    binary_image = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
    return binary_image


def get_contours(binary_image, minArea=100):
    contours, hierarchy = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candy_contours = []

    for idx, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > minArea:
            print(idx, area)
            candy_contours.append(cnt)
    print(f"Total meaningful contours are {len(candy_contours)}")

    return candy_contours


def draw_contours(img, cnt):
    cv2.drawContours(img, cnt, -1, (0, 255, 0), -1)
    cv2.putText(img, f"candies identified : {len(cnt)}",
                (10, 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
    show_image("Drawn Contours", img, 10)


if __name__ == "__main__":
    # Reading and displaying input Image
    vid = cv2.VideoCapture("./images/candies_on_table.mov")

    while True:
        grabbed, frame = vid.read()
        if grabbed:
            binary_image = preprocess_input_img(frame)
            cnts = get_contours(binary_image, 150)
            draw_contours(frame, cnts)
        else:
            print("Video Ended")
            break
