import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

# 영상의 속성 참조
print('type(img1):', type(img1))
print('img1.shape:', img1.shape) # 2차원 (480 세로, 640 가로)
print('img2.shape:', img2.shape) # 3차원
print('img1.dtype:', img1.dtype) # uint8
print('img1.dtype:', img2.dtype) # uint8


# 영상의 크기 참조
h, w = img1.shape
print('w x h = {} x {}'.format(w, h))

# h, w = img2.shape # 3차원인데 2개만 받으려고 하니 오류가 남
# print('w x h = {} x {}'.format(w, h))

h, w = img2.shape[:2]
print('img2 size: {} x {}'.format(w, h))

# grayscale 인지 판단
# if img1.ndim == 2: # if len(img1.shape) == 2:
#     print('img1 is a graysclae image')
    
if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

# 영상의 픽셀 값 참조
# x = 20 y = 10의 픽셀 값 가져옴
x = 20
y = 10
p1 = img1[y,x]
print(p1)
p2 = img2[y,x]
print(p2)

# img1의 모든 픽셀을 그레이스케일 255로 바꿈
# img2의 모든 픽셀을 r = 255로 바꿈
# @@이 방식은 매우 느리기 때문에 실제로는 사용하면 안됨@@
for y in range(h):
    for x in range(w):
        img1[y, x] = 255
        img2[y, x] = (0, 0, 255)        

# 이 방식이 훨씬 빠르게 동작함
# img1[:,:] = 255
# img2[:,:] = (0, 0, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
