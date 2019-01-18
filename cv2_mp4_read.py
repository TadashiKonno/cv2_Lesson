# -*- coding: utf-8 -*-

#import numpy as np
import cv2
cap = cv2.VideoCapture('waterfall.mp4')

while(True):    
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    cv2.imshow('Movie',gray)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

print(cap.get(3))
cap.release()
cv2.destroyWindow('Movie')
