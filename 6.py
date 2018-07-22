import numpy as np
import cv2
from matplotlib import pyplot as plt
import pytesseract

image= cv2.imread('thresh.png',0)
ret,image1 = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
image1 = cv2.dilate(image1,kernel,iterations = 1)
img, contours, hierarchy = cv2.findContours(image1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(image.shape)
print(image.shape[1]/20)
print(image.shape[0]/20)
image2 = image.copy()
maxh =[]
for i in contours:
    x,y,w,h = cv2.boundingRect(i)
    if w < 80 and h < 80 :
        continue
    if w > 0.9*image2.shape[1] and h > 0.9*image2.shape[0]:
        continue
    print(str(x)+ ',' + str(y)+','+ str(w) + ',' + str(h))
    maxh.append(h)
    image3 = cv2.rectangle(image2,(x,y),(x+w,y+h),(0,255,0),1)

print(max(maxh))

plt.imshow(image3, cmap = 'gray', interpolation = 'bicubic')
plt.show()

'''image = cv2.resize(image,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)
_ , image = cv2.threshold(image,0,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)

data = pytesseract.image_to_string(image)
with open('put.txt','w') as f:
    f.write(str(data))'''
