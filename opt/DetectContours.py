import cv2
from matplotlib.pyplot import contour
import numpy as np
import copy

img = cv2.imread("input/fall.jpg")
img_grey = cv2.imread("input/fall.jpg",0)

# 大津の方法による二値化
ret_otsu, img_bi_otsu=cv2.threshold(img_grey, 0, 255, cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(img_bi_otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 入力、輪郭のリスト、描画数、線の色、太さ
img_contours = cv2.drawContours(img, contours, -1, (255,0,0), 1)

cv2.imwrite("output/fall_con.jpg", img_contours)