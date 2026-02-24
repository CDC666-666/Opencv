import cv2
import numpy as np

video_path = '/home/c/桌面/Opencv/video.avi'

cap = cv2.VideoCapture(video_path)

def detect_light_bars(frame):
    """检测灯条部分的函数"""
    # 转换到HSV颜色空间，更好地识别颜色
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 定义红色灯条的颜色范围（HSV空间）
    # 红色在HSV中有两个范围
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    
    # 定义蓝色灯条的颜色范围
    lower_blue = np.array([100, 100, 50])
    upper_blue = np.array([140, 255, 255])
    
    # 创建颜色掩码
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # 合并红色掩码
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    
    # 合并所有灯条颜色掩码
    mask_light = cv2.bitwise_or(mask_red, mask_blue)
    
    # 形态学操作，去除噪声
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask_light = cv2.morphologyEx(mask_light, cv2.MORPH_CLOSE, kernel)
    mask_light = cv2.morphologyEx(mask_light, cv2.MORPH_OPEN, kernel)
    
    return mask_light

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # 检测灯条
    light_mask = detect_light_bars(frame)
    
    # 找到灯条轮廓
    cnts, _ = cv2.findContours(light_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 在原始帧上绘制检测到的灯条
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area > 100:  # 过滤掉太小的区域
            x, y, w, h = cv2.boundingRect(cnt)
            
            # 计算长宽比，灯条通常是细长的
            aspect_ratio = w / h if h != 0 else 0
            if aspect_ratio > 2 or aspect_ratio < 0.5:  # 长宽比筛选
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, 'Light Bar', (x, y-10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 显示结果
    cv2.imshow('Light Bar Detection', frame)
    cv2.imshow('Light Mask', light_mask)
    
    key = cv2.waitKey(30)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

