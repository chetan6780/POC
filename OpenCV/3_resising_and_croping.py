# In opencv y axis is towerds the south (down)
import cv2
import numpy as np


img = cv2.imread('chetan1.jpg')

print(img.shape)  # show the size (h,w, channel for bgr)

img_resize = cv2.resize(img, (400, 300))  # (w,h)
img_cropped = img[:300, 200:500] #(h,w)

print(img_resize.shape)

cv2.imshow('output', img)
# cv2.imshow('resize image',img_resize)
cv2.imshow('cropped image', img_cropped)

cv2.waitKey(0)
