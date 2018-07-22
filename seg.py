'''import cv2
import numpy as np

img = cv2.imread('vedantu-8.png',0)
blur = cv2.GaussianBlur(img,(5,5),0)
ret,blur = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#x_sum = cv2.reduce(blur,0,cv2.REDUCE_SUM,dtype=cv2.CV_32S)
#y_sum = cv2.reduce(blur,1,cv2.REDUCE_SUM,dtype=cv2.CV_32S)
(h, w) = blur.shape[:2]
sumCols = []
for j in range(w):
    col = img[0:h, j:j+1] # y1:y2, x1:x2
    sumCols.append(np.sum(col))
print(sumCols)
cv2.imshow('image',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("a2.jpg",0)
th, threshed = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
pts = cv2.findNonZero(threshed)
ret = cv2.minAreaRect(pts)
print(ret)
(cx,cy), (w,h), ang = ret
if w>h:
    w,h = h,w
    ang += 90
M = cv2.getRotationMatrix2D((cx,cy), ang, 1.0)
rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))

hist = cv2.reduce(rotated,1,cv2.REDUCE_SUM,dtype=cv2.CV_32S).reshape(-1)
th = 3500
H,W = img.shape[:2]
print(H)
print(W)
uppers = [y for y in range(H-1) if hist[y]<=th and hist[y+1]>th]
lowers = [y for y in range(H-1) if hist[y]>th and hist[y+1]<=th]

rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
for y in uppers:
    cv2.line(rotated, (0,y), (W, y), (255,0,0), 1)

for y in lowers:
    cv2.line(rotated, (0,y), (W, y), (0,255,0), 1)

if len(lowers) > len(uppers):
    lowers.pop(0)
if len(uppers) > len(lowers):
    uppers.pop(0)
print(uppers)
print(lowers)
cv2.imshow('imghs',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

j = 0
for y in uppers:
    cv2.imshow('image',img[y:lowers[j],0:W])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    j = j +1'''

import cv2
import numpy as np
img = cv2.imread('vedantu-8.png',0)
gray = cv2.medianBlur(img,5)
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

thresh = cv2.dilate(thresh,None,iterations = 3)
thresh = cv2.erode(thresh,None,iterations = 2)

image, contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# For each contour, find the bounding rectangle and draw it
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.rectangle(thresh_color,(x,y),(x+w,y+h),(0,255,0),2)

# Finally show the image
cv2.imshow('img',img)
cv2.imshow('res',thresh_color)
cv2.waitKey(0)
cv2.destroyAllWindows()