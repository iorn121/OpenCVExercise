import cv2
import numpy as np
from numpy.lib.function_base import average

img=cv2.imread("input/fall.jpg",0)

# (1,2000)のノイズを2つ用意
x = np.random.randint(512, size=2000)
y = np.random.randint(512, size=2000)
# 2000か所の画素を変更
for i,j in zip(x,y):
  img[i][j]=200

# # 平滑化フィルターをかける
# average_kernel=np.ones((10,10))/100.0
# img_smo=cv2.filter2D(img,-1,average_kernel)
img_blur=cv2.blur(img, (10,10))


cv2.imwrite("output/fall_grey_noise.jpg", img)
cv2.imwrite("output/fall_blur.jpg", img_blur)
# cv2.imwrite("output/fall_smo.jpg", img_smo)