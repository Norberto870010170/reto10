import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
verdeInf = np.array([45,100,100])
verdeSup = np.array([65,255,255])
verdeMask = cv2.inRange(HSV,verdeInf,verdeSup)
res = cv2.bitwise_and(img, img, mask=verdeMask)
cv2.imshow('img', img)
cv2.imshow('mask', verdeMask)
cv2.imshow('verde', res)
cv2.waitKey(0)

