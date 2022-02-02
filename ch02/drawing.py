import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

# 시작점, 끝 점 , 색깔, 두께
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

# 우측 상단 점, 우츠 하단 점, 
# 색깔, 두께(두께에 음수를 지정하면 내부를 채운다)
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

# 원의 중심점, 반지름, 두께(음수를 지정하면 내부를 채움), 
# 라인타입(Line_AA를 하면 더 부드럽게 원을 그려줌 default는 line_8)
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 꼭짓점 좌표를 리스트로 전달
# isClosed (True면 시작점과 끝점을 잇고 false면 잇지 않음)
# 색깔, 두께
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2)

# 출력 문자열, 문자열을 출력할 좌측 하단 좌표, 폰트(대부분 simplex),
# fontscale(문자열 크기 지정), 색깔, 두께, 라인타입
text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

