#coding=utf-8

import cv2
import numpy as np

frame=cv2.imread('123.jpg',-1)
cv2.imshow('image',frame)

#BGR模式转换成HSV模式
img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

#--------识别颜色
#红色
mask1=cv2.inRange(img,np.array([0,43,46]),np.array([10,255,255]))
#橙色
mask2=cv2.inRange(img,np.array([11,43,46]),np.array([25,255,255]))
#黄色
mask3=cv2.inRange(img,np.array([26,43,46]),np.array([34,255,255]))
#白色
mask4=cv2.inRange(img,np.array([0,0,221]),np.array([180,30,255]))
mask=mask1+mask2+mask3+mask4

#转回彩色
res=cv2.bitwise_and(frame,frame,mask=mask)

#转成灰度
res=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

#二值化
ret,res = cv2.threshold(res,0,255,cv2.THRESH_BINARY)

#人体颜色占比，占比越大，踢被子趋势越明显
num=cv2.countNonZero(res)/float(res.size)
print num

cv2.imshow('image',res)
if cv2.waitKey(0):cv2.destroyAllWindows()