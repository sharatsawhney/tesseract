from PIL import Image
import pytesseract
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from difflib import SequenceMatcher
import subprocess

image= cv2.imread('vedantu-8.png',0)

#image = img[880:1250,60:800]

image = cv2.resize(image,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)
_ , image = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#subprocess.call(["tesseract","vedantu-1.png","vedant2","hocr"])
data = pytesseract.image_to_string(image)
with open('put3.txt','w') as f:
    f.write(str(data))




'''print('1-2')
for i in range(len(data1)):
    if data1[i] != data2[i]:
        print(i, data1[i], data2[i])

print('1-3')
for i in range(len(data1)):
    if data1[i] != data3[i]:
        print(i, data1[i], data3[i])

print('1-4')
for i in range(len(data1)):
    if data1[i] != data4[i]:
        print(i, data1[i], data4[i])'''

'''rows,cols = image.shape

pts1 = np.float32([[100,100],[800,100],[100,1240],[800,1240]])
pts2 = np.float32([[0,0],[1000,0],[0,1000],[1000,1000]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(image,M,(1000,1000))'''
#dst = cv2.resize(image,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
#_ , dst = cv2.threshold(dst,140,255,cv2.THRESH_BINARY)
#dst = cv2.adaptiveThreshold(dst,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
#ret2,dst = cv2.threshold(dst,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#blur = cv2.GaussianBlur(dst,(5,5),0)
#ret3,dst = cv2.threshold(dst,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''data = pytesseract.image_to_string(image)
with open('put.txt','w') as f:
    f.write(str(data))'''


'''plt.subplot(121),plt.imshow(image),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()'''

'''cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


