import cv2
import numpy as np
import copy

img = cv2.imread("input/ship.jpg")
img_grey = cv2.imread("input/ship.jpg",0)

img_harris = copy.deepcopy(img)

img_dst = cv2.cornerHarris(img_grey, 2, 3, 0.04)

img_harris[img_dst > 0.05 * img_dst.max()] = [255,0,0]

cv2.imwrite("output/ship_har.jpg", img_harris)