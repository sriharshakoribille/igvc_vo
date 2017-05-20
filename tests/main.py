import cv2
import numpy as np 

width, height, fx, fy, cx, cy= np.array([1241.0, 376.0, 718.8560, 718.8560, 607.1928, 185.2157])
pp=(cx,cy)
img_id=1
prev_img= cv2.imread('/home/sriharsha/igvc/tests/KITTI_sample/images/'+str(img_id).zfill(6)+'.png', 0)
kp_prev=featureDetect(prev_img)
img_id=img_id+1
for img_id in xrange(1200):
	next_img = cv2.imread('/home/sriharsha/igvc/tests/KITTI_sample/images/'+str(img_id).zfill(6)+'.png', 0)
	pts_prev,pts_next = featureTracking(prev_img, next_img, kp_prev)
	E, mask = cv2.findEssentialMat(pts_prev, pts_next, focal=fx, pp=pp, method=cv2.RANSAC, prob=0.999, threshold=1.0)
	_, cur_R, cur_t, mask = cv2.recoverPose(E, pts_next, pts_prev, fx, pp = pp)
	

