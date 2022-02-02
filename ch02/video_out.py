import sys
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# fourcc 설정 DIVX 정수값 받아오기.
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
delay = round(1000 / fps) # 프레임 사이 시간 설정

# 출력 비디오 이름, fourcc - 압축 방식, 프레임, 가로 세로
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # inversed = ~frame
    
    # edge는 그레이 스케일로 저장하기 때문에
    # 비디오라이터에 사용하면 정상적으로 실행되지 않는다
    # 따라서 아래의 과정이 필요함
    edge = cv2.Canny(frame, 50, 150)
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    
    # out.write(inversed)
    out.write(edge_color)
    # out.write(frame)

    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
