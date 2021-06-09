import cv2
import numpy as np

gammma=1.5

img=cv2.imread("input/fall.jpg")

gammma_cvt=np.zeros((256,1), dtype='uint8')

for i in range(256):
  gammma_cvt[i][0]=255*(float(i)/255)**(1.0/gammma)

  img_gammma=cv2.LUT(img,gammma_cvt)

  cv2.imwrite("output/fall_gamma.jpg", img_gammma)