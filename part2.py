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


contours,hierarchy = cv2.findContours(thresh,2,1)
cnt = contours[0]

hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()