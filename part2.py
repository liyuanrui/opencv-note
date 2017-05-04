#coding=utf-8

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

os.chdir('C:/Users/LR/Desktop')



img=cv2.imread('123.jpg',0)

kernel=np.ones((5,5),np.uint8)
erosion= cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.imshow('image',erosion)
if cv2.waitKey(0) & 0xFF ==ord('q'):
    cv2.destroyAllWindows()