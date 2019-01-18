# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
#import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("opencv-logo-white.png",cv2.IMREAD_GRAYSCALE)
#print(img)
plt.imshow(img)
plt.show()
#cv2.imshow("Image",img)
#cv2.waitKey(0) & 0xFF
#cv2.destroyAllWindows()
