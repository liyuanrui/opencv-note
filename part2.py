#coding=utf-8

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

os.chdir('C:/Users/LR/Desktop')

BLUE=[255,0,0]

img1=cv2.imread('143.jpg')

#重复，空白
replicate=cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REPLICATE)

#映射，镜面
reflect=cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT_101)

#包围
wrap=cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_WRAP)

constant=cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_CONSTANT,value=BLUE)

cv2.imshow('image',constant)
cv2.waitKey(0)
cv2.destroyAllWindows()