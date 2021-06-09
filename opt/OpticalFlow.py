import cv2
from matplotlib.pyplot import contour, sca
import numpy as np
import copy

count = 500
criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 20, 0.03)
lk_params = dict(winSize=(10,10), maxLevel=4, criteria=criteria)

cap = cv2.VideoCapture("input/river.mp4")
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_rate=int(cap.get(cv2.CAP_PROP_FPS))
frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # ファイル形式
save = cv2.VideoWriter('output/river_opt.mp4', fmt, frame_rate, (width,height)) 
ret, frame = cap.read()
frame_pre =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
save.write(frame)

for i in range(1,frame_count):
  ret, frame = cap.read()
  if ret == False:
    break
  frame_now = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  feature_pre = cv2.goodFeaturesToTrack(frame_pre, count, 0.001,5)
  if feature_pre is None:
    continue
  
  feature_now, status, err = cv2.calcOpticalFlowPyrLK(frame_pre, frame_now, feature_pre, None, **lk_params)

  for i in range(len(feature_now)):
    pre_x = int(feature_pre[i][0][0])
    pre_y = int(feature_pre[i][0][1])
    now_x = int(feature_now[i][0][0])
    now_y = int(feature_now[i][0][1])
    # print(pre_x)
    # print(pre_y)
    # print(now_x)
    # print(now_y)
    cv2.line(frame, (pre_x,pre_y), (now_x,now_y), (255,0,0), 3)

  save.write(frame)

save.release()
cv2.destroyAllWindows()