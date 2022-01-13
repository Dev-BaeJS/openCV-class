import numpy as np
import cv2


# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)       # grayscale image // 쓰레기값을 집어넣음
img2 = np.zeros((240, 320, 3), dtype=np.uint8)    # color image // 모든 픽셀을 0으로
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # dark gray // 모든 픽셀을 1*255로
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow // 모든 픽셀을 

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('HappyFish.jpg')

img2 = img1 # img1 의 주소값을 복사하기 때문에 img1을 수정해도 img2가 수정된다 참조의 개념
img3 = img1.copy() # 메모리를 새로 할당하기 때문에 img1이 수정되어도 영향이 없다

#img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('HappyFish.jpg')

# 40번째 행부터 120번째 행까지 , 30번째 열부터 150번째 열까지
img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

img1[:, :] = (0, 255, 255) # img1의 모든 픽셀을 노란색으로 변경하면 img2도 영향받음

# img2.fill(0)
# img2의 50,50 좌표를 기준으로 반지름이 20이고 색은 빨간색이고 두께는 2의 원을 그려라
cv2.circle(img2, (50,50), 20, (0,0,255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
