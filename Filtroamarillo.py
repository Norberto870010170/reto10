import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
amarilloInf = np.array([25,50,50])
amarilloSup = np.array([45,255,255])
amarilloMask = cv2.inRange(HSV,amarilloInf,amarilloSup)
res = cv2.bitwise_and(img, img, mask=amarilloMask)
cv2.imshow('img', img)
cv2.imshow('mask', amarilloMask)
cv2.imshow('amarillo', res)
cv2.waitKey(0)

