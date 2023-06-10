import cv2
import numpy as np


if __name__ == "__main__" : 

    image = np.zeros((100, 100, 3), dtype = "uint8")
    cv2.imshow("random_image", image)
    cv2.waitKey(-1)
    
    # filling the black space with random color

    for row in range(100):
        for col in range(100):
            for channel in range(3):
                pixel_value = np.random.randint(0,256)
                image[row, col, channel]=pixel_value
    
    cv2.imshow("color_image", image)
    cv2.waitKey(-1)

    # converting color image to binary 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary = np.zeros((100, 100), dtype="uint8")
    for row in range(100):
        for col in range(100):
            if gray[row, col] > 128:
                binary[row, col] = 255
            else:
                binary[row, col] =0
    
    cv2.imshow("binary_image", binary)
    cv2.waitKey(-1)



