import sys
import cv2

print('Hello OpenCV', cv2.__version__)

path = 'C:/Users/CEO/Desktop/openCV/openCV-class/openCV-class/ch01/'
# img = cv2.imread(path +'cat.bmp')
img = cv2.imread(path +'cat.bmp', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread(path +'cat.bmp', cv2.IMREAD_UNCHANGED) # 알파 채널까지 읽어옴
# img = cv2.imread('cat.bmp')

if img is None:
    print('Image load failed!')
    sys.exit()
    
# cv2.imwrite('cat_gray.png', img) # img 파일을 새로 저장하기
    
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)    # 창의 크기에 맞게 변경
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)     # 영상 크기를 찾 크기에 맞게 지정
cv2.imshow('image', img)
key = cv2.waitKey() # 누르는 키의 아스키 코드 값 반환
print(key) 


cv2.destroyAllWindows() # 열려있는 모든 창 닫기
# cv2.destroyWindow('image') # 닫고자 하는 창 이름 입력