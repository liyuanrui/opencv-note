#coding=utf-8

import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),5,cv2.LINE_AA)

cv2.imshow('image',img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


