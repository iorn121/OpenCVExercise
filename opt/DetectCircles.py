import cv2
import numpy as np

img = cv2.imread("input/fall.jpg")
img_grey = cv2.imread("input/fall.jpg",0)

circles = cv2.HoughCircles(img_grey, cv2.HOUGH_GRADIENT, dp=1, minDist=1, param1=20, param2=35, minRadius=1, maxRadius=30)

for x,y,r in circles.squeeze(axis=0).astype(int):
  cv2.circle(img, (x,y), r, (255,0,0), 1)

cv2.imwrite("output/fall_cir.jpg", img)