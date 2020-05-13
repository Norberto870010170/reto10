import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
celesteInf = np.array([90,70,100])
celesteSup = np.array([120,255,255])
celesteMask = cv2.inRange(HSV,celesteInf,celesteSup)
res = cv2.bitwise_and(img, img, mask=celesteMask)
cv2.imshow('img', img)
cv2.imshow('mask', celesteMask)
cv2.imshow('celeste', res)
cv2.waitKey(0)

