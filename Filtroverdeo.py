import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
verdeoInf = np.array([70,100,100])
verdeoSup = np.array([100,255,255])
verdeoMask = cv2.inRange(HSV,verdeoInf,verdeoSup)
res = cv2.bitwise_and(img, img, mask=verdeoMask)
cv2.imshow('img', img)
cv2.imshow('mask', verdeoMask)
cv2.imshow('verdeo', res)
cv2.waitKey(0)

