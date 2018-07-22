import numpy as np
import cv2
from matplotlib import pyplot as plt
import pytesseract
# removes pixels in image that are between the range of
# [lower_val,upper_val]

image= cv2.imread('a2.jpg',0)
ret,image1 = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((7,7),np.uint8)
image1 = cv2.dilate(image1,kernel,iterations = 6)
img, contours, hierarchy = cv2.findContours(image1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(image.shape)
print(image.shape[1]/20)
print(image.shape[0]/20)
for i in contours:
    x,y,w,h = cv2.boundingRect(i)
    print(str(x)+ ',' + str(y)+','+ str(w) + ',' + str(h))
    if w < image.shape[1]/20 or h < image.shape[0]/20:
        continue
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
image = image[3:281,29:1014]
image = cv2.resize(image,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
_ , image = cv2.threshold(image,0,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)

data = pytesseract.image_to_string(image)
with open('puty.txt','w') as f:
    f.write(str(data))
  # to hide tick values on X and Y axis
