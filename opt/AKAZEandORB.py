import cv2
import numpy as np
import copy

img = cv2.imread("input/fall.jpg")
img_grey = cv2.imread("input/fall.jpg",0)
img_akaze = copy.deepcopy(img)

akaze = cv2.AKAZE_create()
kp1 = akaze.detect(img_akaze)
img_akaze = cv2.drawKeypoints(img_akaze, kp1, None)

img_orb = copy.deepcopy(img)

orb = cv2.ORB_create()
kp2 = orb.detect(img_orb)
img_orb = cv2.drawKeypoints(img_orb, kp2, None)

cv2.imwrite("output/fall_AKA.jpg", img_akaze)
cv2.imwrite("output/fall_ORB.jpg", img_orb)