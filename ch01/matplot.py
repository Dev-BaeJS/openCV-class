import matplotlib.pyplot as plt # plt로 이름을 변경
import cv2

path = 'C:/Users/CEO/Desktop/openCV/openCV-class/openCV-class/ch01/'

# 컬러 영상 출력
imgBGR = cv2.imread(path + 'cat.bmp')  # BGR 순서
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # BGR을 RGB로 변환

plt.axis('off') # x축 y축 지우기
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread(path + 'cat.bmp', cv2.IMREAD_GRAYSCALE)

# plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)   
# 1행에 표현하고 2개의 열 중 첫 번째의 열에 그려라
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
# 1행에 표현하고 2개의 열 중 두 번째의 열에 그려라
plt.show()
