import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
naranjaInf = np.array([10,50,50])
naranjaSup = np.array([22,255,255])
naranjaMask = cv2.inRange(HSV,naranjaInf,naranjaSup)
res = cv2.bitwise_and(img, img, mask=naranjaMask)
cv2.imshow('img', img)
cv2.imshow('mask', naranjaMask)
cv2.imshow('naranja', res)
cv2.waitKey(0)

