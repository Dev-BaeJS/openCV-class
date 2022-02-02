import sys
import numpy as np
import cv2


oldx = oldy = -1

# 마우스 이벤트 종류, 이벤트 발생 좌표 x,y, 
# flags - 마우스 이벤트 시 상태 
# (왼쪽, 오른쪽, 가운데 버튼을 누르고 이동하는지
# ctrl, shift, alt 키를 누르고 이동하는지)
# 동시에 다른 상태들도 확인 가능
def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y


img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
# 창 이름, 콜백함수 이름, 전달할 변수
# namedWindow 혹은 imshow가 호출된 뒤에 불려야 함
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
