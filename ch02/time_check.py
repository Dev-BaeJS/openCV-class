import sys
import time
import numpy as np
import cv2


img = cv2.imread('hongkong.jpg')

tm = cv2.TickMeter()

tm.reset()
tm.start() # 방식 1
t1 = time.time() # 방식 2

edge = cv2.Canny(img, 50, 150)

tm.stop()
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

