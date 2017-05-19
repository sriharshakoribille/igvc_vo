import numpy as np
import cv2
from matplotlib import pyplot as plt

kernel = np.ones((5,5),np.uint8)
im = cv2.imread('1.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,100,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0,255,0), 1)
cv2.imshow('Image1',im)