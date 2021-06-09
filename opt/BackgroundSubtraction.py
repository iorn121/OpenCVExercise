import cv2
from matplotlib.pyplot import contour, sca
import numpy as np
import copy

cap = cv2.VideoCapture("input/river.mp4")
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_rate=int(cap.get(cv2.CAP_PROP_FPS))
frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # ファイル形式
save = cv2.VideoWriter('output/river_bgs.mp4', fmt, frame_rate, (width,height)) 

frame_back = np.zeros((height,width,3), dtype=np.float32)


for i in range(frame_count):
  th=100
  ret, frame = cap.read()
  if ret == False:
    break
  frame_diff = cv2.absdiff(frame.astype(np.float32), frame_back)
  cv2.accumulateWeighted(frame, frame_back, 0.03)
  save.write(frame_diff.astype(np.uint8))

save.release()
cv2.destroyAllWindows()