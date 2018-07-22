from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import cv2

image = cv2.imread('a1.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
D = ndimage.distance_transform_edt(thresh)
localMax = peak_local_max(D, indices=False, min_distance=0,labels=thresh)

markers = ndimage.label(localMax,structure=np.ones((3,3)))[0]
labels = watershed(-D, markers, mask = thresh)

for label in np.unique(labels):
    if label == 0:
        continue

    mask = np.zeros(gray.shape, dtype="uint8")
    mask[labels == label] = 255

    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    c = max(contours, key=cv2.contourArea)

    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)

cv2.imshow("Output", image)
cv2.waitKey(0)
