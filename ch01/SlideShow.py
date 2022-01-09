import sys
import glob
import cv2


# 이미지 파일을 모두 img_files 리스트에 추가
# imgaes 폴더 밑에 있는 jpg 파일 모두 불러오기
img_files = glob.glob('.\\images\\*.jpg') 

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

# 전체 화면으로 'image' 창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 무한 루프
cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed!')
        break

    cv2.imshow('image', img)
    # 키를 누르지 않는 이상 1초 정도 기다리기
    # 아무 키를 누르지 않으면 -1 return
    if cv2.waitKey(1000) >= 0:
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()
