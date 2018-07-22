import cv2
import numpy as np
import os

# Load the image
img = cv2.imread('a1.jpg')
# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive threshold ()
thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
# Apply some dilation and erosion to join the gaps
cv2.imshow('image',thresh)
cv2.waitKey(0)

# Find the contours for each WORD
image,contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a folder to store the output files for segmentation
output_folder = "seg_folder/"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

word_count = 0

# Sort the contours for the words
boundingBoxes = [cv2.boundingRect(c) for c in contours]
(contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b: b[1][0], reverse=False))

# Get the characters from inside each word using word's contour
for cnt in contours:
    # Get the word using the original image
    x, y, w, h = cv2.boundingRect(cnt)
    word_img = img[y:y + h]
    word_img = word_img[:, x:x + w]

    # Convert it to grayscale
    word_gray = cv2.cvtColor(word_img, cv2.COLOR_BGR2GRAY)

    # apply thresholding
    word_thresh = cv2.adaptiveThreshold(word_gray, 255, 1, 1, 11, 2)

    # Find contours inside the word, each contour will represent a character
    word_image,word_contours, word_hierarchy = cv2.findContours(word_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boundingBoxes = [cv2.boundingRect(c) for c in word_contours]

    # Sort the contours for each word


    char_count = 0

    # Generate image file corresponding to each character in the word
    for char_cnt in word_contours:
        char_x, char_y, char_w, char_h = cv2.boundingRect(char_cnt)
        char = word_img
        char = char[:, char_x:char_x + char_w]
        height = len(word_img)
        if (char_h < height / 2):  # remove noise
            continue;
        # position the image in center
        if (height < char_w):
            top_border = (char_w - height) / 2;
            bottom_border = (char_w - height - top_border)
            char = cv2.copyMakeBorder(char, top_border, bottom_border, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        if (char_w < height):
            left_border = (height - char_w) / 2
            right_border = (height - char_w - left_border)
            char = cv2.copyMakeBorder(char, 0, 0, left_border, right_border, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        # Our caffe model was trained on 128*128, so we resize the image to the same size
        char = cv2.resize(char, (128, 128))
        cv2.imwrite(output_folder + "word_" + str(word_count) + "char_" + str(char_count) + ".png", char)
        char_count += 1
    word_count += 1

