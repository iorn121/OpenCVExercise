import cv2
import numpy as np

img = cv2.imread("input/fall.jpg")
img_grey = cv2.imread("input/fall.jpg",0)

# Cannyエッジ検出にかける
img_canny =  cv2.Canny(img_grey,300,450)

lines = cv2.HoughLines(img_canny,1, np.pi / 180, 100)

for i in lines[:]:
  rho = i[0][0]
  theta = i[0][1]
  a = np.cos(theta)
  b = np.sin(theta)
  x0 = a * rho
  y0 = b * rho
  x1 = int(x0 + 1000 * (-b))
  y1 = int(y0 + 1000 * (a))
  x2 = int(x0 - 1000 * (-b))
  y2 = int(y0 - 1000 * (a))
  cv2.line(img, (x1,y1), (x2,y2), (255,0,0), 1)

cv2.imwrite("output/fall_lin.jpg", img)