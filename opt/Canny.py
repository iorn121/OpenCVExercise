import cv2
import numpy as np

img=cv2.imread("input/fall.jpg",0)

img_can=cv2.Canny(img, 100, 200)
cv2.imwrite("output/fall_can.jpg", img_can)