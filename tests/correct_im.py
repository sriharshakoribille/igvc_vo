import cv2
import numpy as np 

def undistort(img):
	cv2.undistort2(img,op,cam_mat,coeffs)
	return op;
