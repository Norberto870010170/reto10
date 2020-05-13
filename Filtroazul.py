import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
azulInf = np.array([100,120,120])
azulSup = np.array([140,255,255])
azulMask = cv2.inRange(HSV,azulInf,azulSup)
res = cv2.bitwise_and(img, img, mask=azulMask)
cv2.imshow('img', img)
cv2.imshow('mask', azulMask)
cv2.imshow('azul', res)
cv2.waitKey(0)

