import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rojolInf = np.array([170,100,100])
rojolSup = np.array([179,255,255])
rojolInf2 = np.array([0,100,100])
rojolSup2 = np.array([10,255,255])
rojoMask = cv2.inRange(HSV,rojolInf2,rojolSup2)
rojoMask2 = cv2.inRange(HSV,rojolInf,rojolSup)
rojoMask3 = rojoMask + rojoMask2
res = cv2.bitwise_and(img, img, mask=rojoMask3)
cv2.imshow('img', img)
cv2.imshow('mask', rojoMask3)
cv2.imshow('rojo', res)
cv2.waitKey(0)

