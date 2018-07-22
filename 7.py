import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('texto.png',0)

surf = cv2.xfeatures2d.SURF_create(3000)
kp, des = surf.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()