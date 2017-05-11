#coding=utf-8

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

os.chdir('C:/Users/LR/Desktop')


#加载灰度图像


img=cv2.imread('333.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv2.imshow('image',hist)
if cv2.waitKey(0) & 0xFF ==ord('q'):
    cv2.destroyAllWindows()