import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
magentaInf = np.array([140,100,20])
magentaSup = np.array([153,255,255])
magentaMask = cv2.inRange(HSV,magentaInf,magentaSup)
res = cv2.bitwise_and(img, img, mask=magentaMask)
cv2.imshow('img', img)
cv2.imshow('mask', magentaMask)
cv2.imshow('magenta', res)
cv2.waitKey(0)

