import cv2
import numpy as np

img=cv2.imread("input/fall.jpg",0)

# 大津の方法によって二値化
ret, img_bi=cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)


# モルフォロジー変換のためのカーネル準備
kernel = np.ones((5,5), dtype=np.uint8)

# 膨張
img_d = cv2.dilate(img_bi,kernel)
cv2.imwrite("output/fall_dilate.jpg", img_d)

# 収縮
img_e = cv2.erode(img_bi,kernel)
cv2.imwrite("output/fall_erode.jpg", img_e)

# オープニング
img_open=cv2.morphologyEx(img_bi, cv2.MORPH_OPEN, kernel)
cv2.imwrite("output/fall_open.jpg",img_open)

# クロージング
img_close=cv2.morphologyEx(img_bi, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("output/fall_close.jpg",img_close)