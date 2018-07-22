import cv2
import numpy as np

im = cv2.imread('a1.jpg',0)
im = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
kernel = np.ones((5,5),np.uint8)
im = cv2.dilate(im,kernel,iterations = 1)
#im = cv2.resize(im,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
params = cv2.SimpleBlobDetector_Params()
params.filterByColor = True
params.blobColor = 255
params.filterByCircularity = True
params.minCircularity = 0.0
detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(im)

im_with_keypoints = cv2.drawKeypoints(im,keypoints,np.array([]),(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)