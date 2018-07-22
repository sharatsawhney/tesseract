from collections import namedtuple
from skimage.filters import threshold_local
from skimage import segmentation
from skimage import measure
import numpy as np
import cv2
import imutils

image = cv2.imread('a1.jpg',0)

thresh = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
labels = measure.label(thresh,neighbors=8,background=0)
charCandidates = np.zeros(thresh.shape,dtype="uint8")

for label in np.unique(labels):
    if label == 0:
        continue

    labelMask = np.zeros(thresh.shape, dtype="uint8")
    labelMask[labels == label] = 255
    cnts = cv2.findContours(labelMask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        (boxX, boxY, boxW, boxH) = cv2.boundingRect(c)

        aspectRatio = boxW / float(boxH)
        solidity = cv2.contourArea(c) / float(boxW * boxH)
        heightRatio = boxH / float(image.shape[0])

        keepAspectRatio = aspectRatio < 1.0
        keepSolidity = solidity > 0.15
        keepHeight = heightRatio > 0.4 and heightRatio < 0.95

        if keepAspectRatio and keepSolidity and keepHeight:
            hull = cv2.convexHull(c)
            cv2.drawContours(charCandidates, [hull], -1, 255, -1)




cv2.imshow('image',charCandidates)
cv2.waitKey(0)
cv2.destroyAllWindows()