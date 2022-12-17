import cv2

# ----------------------------------------------------------------------------------------
'''showing img on screen'''

# # imread reads the img
# img=cv2.imread('location.jpg')

# # imshow shows the img
# cv2.imshow('output',img)

# # waitKey=0 is infinite and 1000 is 1 sec,etc continue
# cv2.waitKey(0)

# ----------------------------------------------------------------------------------------

'''showing video'''
# cap = cv2.VideoCapture("Tenki no ko.webm")

# # video is a sequence of imgs
# while True:
#     # success is true or false
#     success, img = cap.read()
#     cv2.imshow('video', img)

#     # Quits if we press 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# ----------------------------------------------------------------------------------------
'''using the webcam'''
# id 0 = default webcam if you have more then we can add go along
cap = cv2.VideoCapture(0)
# setting width(id=3) and height(id = 4) ,brightness(id=10)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    # success is true or false
    success, img = cap.read()
    cv2.imshow('video', img)

    # Quits if we press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
