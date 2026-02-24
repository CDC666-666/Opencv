import cv2
import numpy as np

curshape = 0
startpos = (0,0)

img = cv2.imread('/home/c/桌面/Opencv/test_1.jpg')
def mousecallback(event, x, y, flags, param):
    global curshape, startpos
    if event == cv2.EVENT_LBUTTONDOWN:
        startpos = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        if curshape == 0:
            cv2.line(img, startpos, (x, y), (0, 0, 255), 3)
        elif curshape == 1:
            cv2.rectangle(img, startpos, (x, y), (0, 0, 255), 3)
        elif curshape == 2:
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a**2 + b**2)**0.5)
            cv2.circle(img, startpos, r, (0, 0, 255))

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img', mousecallback)

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):
        curshape = 0
    elif key == ord('r'):
        curshape = 1
    elif key == ord('c'):
        curshape = 2

cv2.destroyAllWindows()