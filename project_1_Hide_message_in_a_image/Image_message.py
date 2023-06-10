import cv2
import numpy as np


if __name__ == "__main__":
    image = cv2.imread("OpenCV_Fundamentals/project_1_Hide_message_in_a_image/images/monalisa.jpg")
    cv2.imshow("output", image)
    cv2.waitKey(-1)

    # Setting up hidden message to encode 
    message = "We are in position, send in the infantry !  " * 3

    # encoding message in the image
    encoding_row = 1000
    col_count = 0
    for character in message:
        image[encoding_row, col_count] = [ord(character), ord(character), ord(character)]
        col_count += 1
    
    # saving encoded image
    cv2.imwrite("OpenCV_Fundamentals/project_1_Hide_message_in_a_image/images/secret_message.png", image)

    # extracting encoded message
    decoded_msg = ""

    for col in image[1000]:
        decoded_msg = decoded_msg + chr(col[0])
    
    print("--------------")
    print(decoded_msg)



