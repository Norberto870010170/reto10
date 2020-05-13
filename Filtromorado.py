import cv2
import numpy as np
img = cv2.imread("colorBalls.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
moradoInf = np.array([157,153,20])
moradoSup = np.array([160,255,255])
morado2Inf = np.array([165,153,20])
morado2Sup = np.array([170,255,255])
moradoMask = cv2.inRange(HSV,moradoInf,moradoSup)
morado2Mask = cv2.inRange(HSV,morado2Inf,morado2Sup)
moradoMask3 = moradoMask + morado2Mask
res = cv2.bitwise_and(img, img, mask=moradoMask3)
cv2.imshow('img', img)
cv2.imshow('mask', moradoMask3)
cv2.imshow('morado', res)
cv2.waitKey(0)

