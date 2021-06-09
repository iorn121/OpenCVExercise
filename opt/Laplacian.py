import cv2
import numpy as np

img = cv2.imread("input/fall.jpg",0)

img_lap=cv2.Laplacian(img, cv2.CV_32F)

img_lap=cv2.convertScaleAbs(img_lap)

cv2.imwrite("output/fall_lap.jpg", img_lap)