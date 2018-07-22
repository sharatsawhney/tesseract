import numpy as np
import cv2
from matplotlib import pyplot as plt
pure = cv2.imread('a1.jpg')
img = cv2.imread('a1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
#opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)

sure_bg = cv2.dilate(thresh,kernel,iterations=3)

dist_transform = cv2.distanceTransform(thresh,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.3*dist_transform.max(),255,0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
img = cv2.subtract(img,pure)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
image, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2 = img.copy()
maxh =[]
j = 0
for i in contours:
    x,y,w,h = cv2.boundingRect(i)
    #if w < 80 and h < 80 :
     #   continue
    #if w > 0.9*image2.shape[1] and h > 0.9*image2.shape[0]:
     #   continue
    print(str(x)+ ',' + str(y)+','+ str(w) + ',' + str(h))
    cv2.imwrite('char/'+ str(j) + '.jpg',image[y:y+h,x:x+w])
    maxh.append(h)
    image3 = cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),1)
    j = j+1
print(max(maxh))

cv2.imshow('window',image3)
cv2.waitKey(0)
cv2.destroyAllWindows()
