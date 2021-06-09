import cv2
from matplotlib.pyplot import contour, sca
import numpy as np
import copy

criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 10, 1)
rct = (1150,900,50,50)

cap = cv2.VideoCapture("input/river.mp4")
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_rate=int(cap.get(cv2.CAP_PROP_FPS))
frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # ファイル形式
save = cv2.VideoWriter('output/river_cam.mp4', fmt, frame_rate, (width,height)) 


for i in range(frame_count):
  th=100
  ret, frame = cap.read()
  if ret == False:
    break
  frame_now = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  ret, img_bin = cv2.threshold(frame_now, th, 255, cv2.THRESH_BINARY)
  
  ret, rct = cv2.meanShift(img_bin, rct, criteria)
  x,y,w,h = rct
  cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
  save.write(frame)

save.release()
cv2.destroyAllWindows()