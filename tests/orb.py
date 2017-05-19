import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread('board.jpg',0)
cap=cv2.VideoCapture(0)
while(True):

	ret,img=cap.read()
#def features(img)
# Initiate STAR detector
	orb = cv2.ORB_create(nfeatures=20000)

		# find the keypoints with ORB
	kp = orb.detect(img,None)

		# compute the descriptors with ORB
	kp, des = orb.compute(img, kp)
	#return kp,des
	# draw only keypoints location,not size and orientation
	img2 = cv2.drawKeypoints(img,kp,None,color=(0,255,0), flags=0)
	#plt.imshow(img2),plt.show()
	cv2.imshow('sfs',img2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()

