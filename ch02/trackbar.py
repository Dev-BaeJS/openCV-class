import numpy as np
import cv2

# pos는 트랙바 위치
def on_level_change(pos):
    value = pos * 16
    
    value = np.clip(value, 0, 255)
    # if value >= 255:
    #     value = 255

    img[:] = value
    cv2.imshow('image', img)


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
# 트랙바 이름, 트랙바 생성할 창 이름, 트랙바 초기 위치값,
# 최댓값(최솟값은 항상 0) 트랙바 콜백함수 이름
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
