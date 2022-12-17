import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('location.png')

# myData = []
# for barcode in decode(img):
#     myData = [19.00045, 17.00001, 4.00]
#     # myData = barcode.data.decode('utf-8')
# print(myData)
# latitude = myData[0]
# longitude = myData[1]
# altitude = myData[2]
# print(latitude)
# print(longitude)
# print(altitude)

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

myData=[]
while True:
    success, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        myData = barcode.data
        print(myData)

        latitude,longitude,altitude = myData[0],myData[1],myData[2]
        print(latitude)
        print(longitude)
        print(altitude)
    

    cv2.imshow('Result', img)
    cv2.waitKey(1)

