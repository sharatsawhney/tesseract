import numpy as np
import cv2
from matplotlib import pyplot as plt

image= cv2.imread('a1.jpg',0)
#image = cv2.resize(image,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
ret,image1 = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#kernel = np.ones((3,3),np.uint8)
#image1 = cv2.dilate(image1,kernel,iterations = 1)
img, contours, hierarchy = cv2.findContours(image1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
rect = []
for ctr in contours:
    rect.append(cv2.boundingRect(ctr))
rect.sort(key = lambda cnt:cnt[1])
print(rect)
line_bottom = rect[0][1] + rect[0][3] - 1
line_begin_idx = 0
for i in range(len(rect)):
    if rect[i][1] > line_bottom:
        rect[line_begin_idx:i] = sorted(rect[line_begin_idx:i],key = lambda cnt: cnt[0])
        line_begin_idx = i

    line_bottom = max(rect[i][1]+rect[i][3]-1, line_bottom)
rect[line_begin_idx:] = sorted(rect[line_begin_idx:],key=lambda cnt: cnt[0])
print(image.shape)
print(image.shape[1]/20)
print(image.shape[0]/20)
image2 = image.copy()
maxh =[]
j = 0
for i in rect:
    x = i[0]
    y = i[1]
    w = i[2]
    h = i[3]
    #if w < 80 and h < 80 :
     #   continue
    #if w > 0.9*image2.shape[1] and h > 0.9*image2.shape[0]:
     #   continue
    print(str(x)+ ',' + str(y)+','+ str(w) + ',' + str(h))
    cv2.imwrite('char/'+ str(j) + '.jpg',image[y:y+h,x:x+w])
    maxh.append(h)
    image3 = cv2.rectangle(image2,(x,y),(x+w,y+h),(0,255,0),1)
    j = j+1
print(max(maxh))

cv2.imshow('window',image3)
cv2.waitKey(0)
cv2.destroyAllWindows()
