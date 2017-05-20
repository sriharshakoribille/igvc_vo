import cv2
import numpy as np 

def featureDetect(img):
	orb = cv2.ORB_create(nfeatures=2000)
	kp = orb.detect(img,None)
	return kp

def featureTracking(prev_im,next_im,points):
	kp2,st,err=cv2.calcOpticalFlowPyrLK(prev_im, next_im ,points,None,**lk_params)
	st = st.reshape(st.shape[0])
	kp1 = points[st == 1]
	kp2 = kp2[st == 1]
	return kp1,kp2

