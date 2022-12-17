import cv2
import numpy as np

img = cv2.imread('chetan1.jpg')
kernel = np.ones((5, 5), np.uint8)

# convert in color.In opencv colores are in BGR
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)#7 must be odd
img_canny = cv2.Canny(img, 100, 100)  # can go higher or lower thna 100
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
img_erode = cv2.erode(img_dilation, kernel, iterations=1) # opposite to dilation

cv2.imshow("gray img", img_gray)
cv2.imshow("blur img", img_blur)
cv2.imshow("Canny img", img_canny)
cv2.imshow("Dilation img", img_dilation)
cv2.imshow("Eroded img", img_erode)

cv2.waitKey(0)
