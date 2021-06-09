import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

img=cv2.imread("input/fall.jpg")
img_grey=cv2.imread("input/fall.jpg",0)

# 閾値の設定
threshold=100

# 二値化
ret, img_bi=cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
ret_grey, img_grey_bi=cv2.threshold(img_grey, threshold, 255, cv2.THRESH_BINARY)

# 大津の方法による二値化
ret_otsu, img_bi_otsu=cv2.threshold(img_grey, 0, 255, cv2.THRESH_OTSU)

# アダプティブ閾値
img_bi_ada=cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -5)

cv2.imwrite("output/fall_bi.jpg", img_bi)
cv2.imwrite("output/fall_grey_bi.jpg", img_grey_bi)
cv2.imwrite("output/fall_bi_otsu.jpg", img_bi_otsu)
cv2.imwrite("output/fall_bi_ada.jpg", img_bi_ada)
