import cv2
import numpy as np

img=cv2.imread("input/fall.jpg",0)

# Sobelフィルター
img_sobel_x=cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
img_sobel_y=cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)

img_sobel_x=cv2.convertScaleAbs(img_sobel_x)
img_sobel_y=cv2.convertScaleAbs(img_sobel_y)

cv2.imwrite("output/fall_sobel_x.jpg", img_sobel_x)
cv2.imwrite("output/fall_sobel_y.jpg", img_sobel_y)