import sys
import cv2


# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
# 속성 값 참조 프레임 가로,세로 크기, 
# 초당 프레임 수, 총 프레임 수 , 현재 프레임 번호, 노출
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# # 받아올 가로 세로 크기 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 카메라 프레임 처리
while True:
    # ret는 불러왔는지 못 불렀는지 확인
    # frame은 이미지
    # 순서 중요!!!
    ret, frame = cap.read()

    # 동영상이 끝까지 재생됐을 경우 종료
    if not ret:
        break
    
    # 엣지 세팅
    edge = cv2.Canny(frame, 50, 150)
    # inversed = ~frame  # 반전
    
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    # cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27: # ESC
        break

cap.release()
cv2.destroyAllWindows()
