import cv2
from matplotlib.pyplot import contour, sca
import numpy as np
import copy

size=(1024,1024)
cap = cv2.VideoCapture("input/capture.mp4")
frame_rate=int(cap.get(cv2.CAP_PROP_FPS))
frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # ファイル形式
save = cv2.VideoWriter('output/capture_det.mp4', fmt, frame_rate, size) 

for i in range(frame_count):
  ret, frame = cap.read()
  if ret == False:
    break
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # HSV色空間に変換してマスクを作成
  # red
  hsv_min1 = np.array([0,50,50])
  hsv_max1 = np.array([9,255,255])
  mask1 = cv2.inRange(hsv,hsv_min1,hsv_max1)

  hsv_min2 = np.array([159,50,50])
  hsv_max2 = np.array([180,255,255])
  mask2 = cv2.inRange(hsv,hsv_min2,hsv_max2)

  mask = mask1+mask2  

  
  frame_mask=cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
  dst = cv2.bitwise_and(frame,frame_mask)

  save.write(dst)

save.release()
cv2.destroyAllWindows()