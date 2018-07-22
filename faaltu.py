import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',0)

cv2.imshow('img',img)
cv2.waitKey(0)
