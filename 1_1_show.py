import cv2

# 创建一个窗口
cv2.namedWindow('new', cv2.WINDOW_NORMAL)
cv2.resizeWindow('new', 640, 480)

# 显示一个黑色图像
cv2.imshow('new', 0)

# 等待按键
key = cv2.waitKey(0)
if key == ord('q'):
    exit()

cv2.destroyAllWindows()