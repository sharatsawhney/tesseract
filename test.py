import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import feature

image = cv2.imread('vedantu-8.png',0)
img = image.copy()

#img = cv2.resize(img,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)
_ ,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)
#img = cv2.erode(img,kernel,iterations = 3)
img = cv2.dilate(thresh,kernel,iterations = 2)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

'''image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255,255), 2)'''
img = img[0:100]
result = feature.greycomatrix(img, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4],levels=256)
contrast = feature.greycoprops(result,'homogeneity')
print(contrast)
cv2.imshow('image',img)
cv2.waitKey(0)
