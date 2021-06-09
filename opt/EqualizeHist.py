import cv2
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import _nonzero_dispatcher
plt.style.use("ggplot")


img=cv2.imread("input/fall.jpg",0)
hist=cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.ylabel("dot value")
plt.xlabel("freqency")
cv2.imwrite("output/fall_grey.jpg", img)
plt.savefig("output/fall_grey_hist.jpg")

# ヒストグラムを均一化
img_eq=cv2.equalizeHist(img)
hist_eq=cv2.calcHist([img_eq], [0], None, [256], [0,256])
plt.plot(hist_eq)
plt.ylabel("dot value")
plt.xlabel("freqency")

cv2.imwrite("output/fall_eq.jpg", img_eq)
plt.savefig("output/fall_eq_hist.jpg")