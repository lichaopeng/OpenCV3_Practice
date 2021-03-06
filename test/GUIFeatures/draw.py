# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# lineType = cv2.LINE_AA for opencv3
cv2.line(img,(0,0),(511,511),color=(255,0,0),thickness=2,lineType=cv2.LINE_AA)

cv2.rectangle(img,(384,0),(510,128),(0,255,0),1)

cv2.circle(img,(447,63), 62, (0,0,255), -1, lineType=cv2.LINE_AA)

cv2.ellipse(img,(256,256),(100,50),20,0,360,255,-1, lineType=cv2.LINE_AA)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255), lineType=cv2.LINE_AA)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey (0)
cv2.destroyAllWindows()