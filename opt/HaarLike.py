import cv2
import numpy as np
import copy

img = cv2.imread("input/shirakawago.jpg")
img_grey = cv2.imread("input/shirakawago.jpg",0)

HAAR_FILE = "src/haarcascade_frontalface_default.xml"

cascade = cv2.CascadeClassifier(HAAR_FILE)

face = cascade.detectMultiScale(img)

for x, y, w, h in face:
  cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 1)

cv2.imwrite("output/shirakawago_haar.jpg", img)

