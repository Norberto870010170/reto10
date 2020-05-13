import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rosaInf = np.array([160,153,20])
rosaSup = np.array([170,255,255])
rosaMask = cv2.inRange(HSV,rosaInf,rosaSup)
res = cv2.bitwise_and(img, img, mask=rosaMask)
cv2.imshow('img', img)
cv2.imshow('mask', rosaMask)
cv2.imshow('rosa', res)
cv2.waitKey(0)

