#!/usr/bin/env python


'''
This is a boiler plate script that contains an example on how to subscribe a rostopic containing camera frames 
and store it into an OpenCV image to use it further for image processing tasks.
Use this code snippet in your code or you can also continue adding your code in the same file
'''


from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import rospy

class image_proc():

	# Initialise everything
	def _init_(self):
		rospy.init_node('barcode_test') #Initialise rosnode 
		self.image_sub = rospy.Subscriber("/edrone/camera/image_raw", Image, self.image_callback) 
        #Subscribing to the camera topic
		self.img = np.empty([]) # This will contain your image frame from camera
		self.bridge = CvBridge()


	# Callback function of camera topic
	def image_callback(self, data):
		try:
			self.img = self.bridge.imgmsg_to_cv2(data, "bgr8") # Converting the image to OpenCV standard image
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
		except CvBridgeError as e:
			print(e)
			return

if _name_ == '_main_':
    image_proc_obj = image_proc()
    rospy.spin()