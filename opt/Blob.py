import cv2
from matplotlib.pyplot import contour, sca
import numpy as np
import copy

img = cv2.imread("input/fall.jpg")
img_grey = cv2.imread("input/fall.jpg",0)


# 大津の方法による二値化
ret_otsu, img_bi_otsu=cv2.threshold(img_grey, 0, 255, cv2.THRESH_OTSU)


nLabels, labelImage, stats, centroids = cv2.connectedComponentsWithStats(img_bi_otsu)

img_blob = copy.deepcopy(img)
h,w = img_grey.shape
color = [[255,0,0], [0,255,0], [0,0,255], [255,255,0]]

# for y in range(h):
#   for x in range(w):
#     if labelImage[y,x] > 0:
#       img_blob[y,x] = color[labelImage[y,x]-1]

for i in range(1,nLabels):
  xc = int(centroids[i][0])
  yc = int(centroids[i][1])
  font = cv2.FONT_HERSHEY_COMPLEX
  scale = 1
  color = (255,255,255)
  cv2.putText(img_blob, str(stats[i][-1]), (xc,yc), font, scale, color)

cv2.imwrite("output/fall_blob.jpg", img_blob)