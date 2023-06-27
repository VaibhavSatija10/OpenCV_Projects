
import cv2
import numpy

#Read the image and convert it to grayscale

image = cv2.imread('Box.jpeg')
image = cv2.resize(image, None, fx=0.5, fy=0.5)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Now convert the grayscale image to binary image

ret, binary = cv2.threshold (gray, 0, 255, cv2. THRESH_BINARY+cv2. THRESH_OTSU)

#Now detect the contours
contours, hierarchy = cv2.findContours (binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

#Visualize the data structure
print("Length of contours {}".format(len(contours)))
print(contours)

# draw contours on the original image
image_copy = image.copy()
image_copy = cv2.drawContours (image_copy, contours, -1, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

#Visualizing the results
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Drawn Contours', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Binary Image', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Certainly! This code is written in Python using the OpenCV library, which is commonly used for computer vision tasks. Let's go through the code step by step:

Importing the necessary libraries:

cv2: This library provides functions for image processing and computer vision operations.
numpy: This library is used for numerical operations and array manipulation.
Reading and resizing the image:

The code reads an image file named "Box.jpeg" using the cv2.imread() function.
The image is then resized to 50% of its original size using cv2.resize() and assigned to the image variable.
Converting the image to grayscale:

The cv2.cvtColor() function converts the image from BGR (Blue-Green-Red) color space to grayscale using the cv2.COLOR_BGR2GRAY conversion code.
The resulting grayscale image is stored in the gray variable.
Converting the grayscale image to binary:

The cv2.threshold() function is used to convert the grayscale image to a binary image. It applies a thresholding technique called Otsu's method (cv2.THRESH_OTSU) to automatically determine the optimal threshold value.
The thresholded image is stored in the binary variable, and the threshold value is stored in the ret variable.
Detecting contours:

The cv2.findContours() function detects contours in the binary image. It takes the binary image, contour retrieval mode (cv2.RETR_TREE), and contour approximation method (cv2.CHAIN_APPROX_NONE) as parameters.
The function returns the contours and the hierarchy (relationships between contours) as output, which are assigned to the contours and hierarchy variables, respectively.
Visualizing the data structure:

The code prints the length of the contours list, which represents the number of contours detected.
It also prints the entire contours list, which contains the coordinates of the contour points.
Drawing contours on the original image:

A copy of the original image is created using image.copy() and assigned to the image_copy variable.
The cv2.drawContours() function is used to draw the contours on the image_copy. It takes the image, contours, contour index (-1 to draw all contours), color (0, 255, 0 - green), thickness (2 pixels), and line type (cv2.LINE_AA) as parameters.
The updated image with drawn contours is stored in the image_copy variable.
Visualizing the results:

The grayscale image, drawn contours on the original image, and the binary image are displayed in separate windows using the cv2.imshow() function.
The code waits for a key press (cv2.waitKey(0)) before closing the windows and terminating the program.
That's an overview of the code, which reads an image, converts it to grayscale, applies thresholding, detects contours, and visualizes the results.
'''