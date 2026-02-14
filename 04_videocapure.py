import cv2

cv2.namedWindow('video', cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()

    cv2.imshow('video',frame)

    key = cv2.waitKey(10)
    if(key & 0xFF== ord('q')):
      break

cap.release()
cv2.destoryALLWindows()
'''import cv2

# 尝试打开摄像头（通常为 0）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头！")
else:
    print("摄像头已打开！")

    # 读取一帧看看
    ret, frame = cap.read()
if ret:
    print("Frame shape:", frame.shape)
    print("Frame mean pixel value:", frame.mean())  # 如果接近 0，就是黑的
    cv2.imshow('Test', frame)
    if ret:
        print("成功读取帧！")
        cv2.imshow('Test', frame)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    else:
        print("读取帧失败！")

cap.release()'''
