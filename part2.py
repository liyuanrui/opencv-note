#coding=utf-8

import numpy as np
import cv2

#创建一个长宽512的黑色图片
img=np.zeros((512,512,3),np.uint8)

#画一条坐标(0,0)到(511,511)的蓝色直线，厚度为5
img=cv2.line(img,(0,0),(511,511),(255,0,0),5)


cv2.imshow('image',img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


