import cv2
import numpy as np 

a=cv2.imread('/home/sriharsha/igvc/tests/data/board.jpg')
#a=cv2.imread('board.jpg')
cv2.imshow('heh',a)

if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()
