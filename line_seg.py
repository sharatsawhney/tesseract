import cv2
import numpy as np

img = cv2.imread('a1.jpg',0)
height = img.shape[0]
width = img.shape[1]

src_img = cv2.resize(img, dsize =(1320, int(1320*height/width)), interpolation = cv2.INTER_AREA)
height = src_img.shape[0]
width = src_img.shape[1]
thresh = cv2.adaptiveThreshold(src_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)


count_x = np.zeros(shape= (height))
for y in range(height):
    for x in range(width):
        if thresh[y][x] == 255 :
            count_x[y] = count_x[y]+1

local_minima = []
for y in range(len(count_x)):
    if y >= 10 and y <= len(count_x)-11:
        arr1 = count_x[y-10:y+10]
    elif y < 10:
        arr1 = count_x[0:y+10]
    else:
        arr1 = count_x[y-10:len(count_x)-1]
    if min(arr1) == count_x[y]:
        local_minima.append(y)

final_local = []
init = []
end = []
for z in range(len(local_minima)):
    if z != 0 and z!= len(local_minima)-1:
        if local_minima[z] != (local_minima[z-1] +1) and local_minima[z] != (local_minima[z+1] -1):
            final_local.append(local_minima[z])
        elif local_minima[z] != (local_minima[z-1] + 1) and local_minima[z] == (local_minima[z+1] -1):
            init.append(local_minima[z])
        elif local_minima[z] == (local_minima[z-1] + 1) and local_minima[z] != (local_minima[z+1] -1):
            end.append(local_minima[z])
    elif z == 0:
        if local_minima[z] != (local_minima[z+1]-1):
            final_local.append(local_minima[z])
        elif local_minima[z] == (local_minima[z+1]-1):
            init.append(local_minima[z])
    elif z == len(local_minima)-1:
        if local_minima[z] != (local_minima[z-1]+1):
            final_local.append(local_minima[z])
        elif local_minima[z] == (local_minima[z-1]+1):
            end.append(local_minima[z])
for j in range(len(init)):
    mid = (init[j] + end[j])/2
    if (mid % 1) != 0:
        mid = mid+0.5
    final_local.append(int(mid))

final_local = sorted(final_local)

for y in final_local:
    thresh[y][:] = 255

cv2.imshow('image',thresh)
cv2.waitKey(0)