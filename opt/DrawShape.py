import cv2
import numpy as np

# generate original image
img = np.ones((500,500,3), dtype=np.uint8)*255

# draw line
cv2.line(img, (10,10), (300,400), (255,0,0),3)

# draw rectangle
cv2.rectangle(img, (20,100), (50,400), (0,255,0), 5)

# draw circle
cv2.circle(img, (200,100), 20, (0,0,255), 2)

# draw elipse
cv2.ellipse(img, (250,250), (100,50), 20, 180, 45, (128,128,128),1)

# write text
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "Hello OpenCV", (0,200), font, 2, (255,255,0), 5, cv2.LINE_AA)

cv2.imwrite("output/DrawShape.jpg", img)