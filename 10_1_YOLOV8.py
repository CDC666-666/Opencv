from ultralytics import YOLO
import cv2

# 创建可调整大小的窗口
cv2.namedWindow('Pose Detection', cv2.WINDOW_NORMAL)
# 设置窗口初始大小
cv2.resizeWindow('Pose Detection', 800, 600)

# 加载模型
#model = YOLO('./runs/pose/Triangle_215/n_pretrain/weights/yolov8n-pose.pt')
model = YOLO('./runs/pose/Triangle_215/n_pretrain/weights/best.pt')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法读取摄像头帧")
        break

    # 预测
    results = model(frame)

    # 显示结果
    annotated_frame = results[0].plot()
    cv2.imshow('Pose Detection', annotated_frame)

    # 关键修复：将 waitKey(0) 改为 waitKey(1) 实现实时显示
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("程序已退出")