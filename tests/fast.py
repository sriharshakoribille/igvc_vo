import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('board.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp,None, color=(255,0,0))

# Print all default params
#print "Threshold: ", fast.getInt('threshold')
#print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
#print "neighborhood: ", fast.getInt('type')
#print "Total Keypoints with nonmaxSuppression: ", len(kp)

cv2.imshow('fast_true.png',img2)

# Disable nonmaxSuppression
fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)

print "Total Keypoints without nonmaxSuppression: ", len(kp)
cv2.drawKeypoints(img, kp,None)

cv2.imhshow('fast_false.png',img3)