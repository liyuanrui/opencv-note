#coding=utf-8

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

os.chdir('C:/Users/LR/Desktop')


#加载灰度图像
img=cv2.imread('1234.png',0)

#二值化，注意这里最后一个参数用0也可以
ret,thresh=cv2.threshold(img,127,255,0)


contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow('image',contours)
#if cv2.waitKey(0) & 0xFF ==ord('q'):
#    cv2.destroyAllWindows()
