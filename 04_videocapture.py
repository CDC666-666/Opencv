import cv2

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter('/home/cdc/桌面/C++/out2.avi',fourcc,25,(640,480))

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

cap = cv2.VideoCapture(0)
#用于分辨电脑摄像头的分辨率
'''actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"实际分辨率: {actual_width} x {actual_height}")'''

while cap.isOpened():
    ret,frame = cap.read()

    if ret ==True:
        cv2.imshow('video',frame)
        cv2.resizeWindow('video',640,480)
        #写数据到多媒体文件
        vw.write(frame)
        #退出
        key = cv2.waitKey(25)
        if(key & 0xFF== ord('q')):
            break
    else:
        break

cap.release()
vw.release()
cv2.destroyAllWindows()

#判断电脑摄像头是否正常
'''import cv2

# 尝试打开摄像头（通常为 0)
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
