import cv2
import numpy as np

#canny算子：Canny（image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None）
#使用高斯滤波器5✖5对图像进行平滑处理，然后计算图像的梯度强度和方向，最后应用非极大值抑制和双阈值检测来检测图像中的边缘

img = cv2.imread("/home/c/桌面/Opencv/test_1.jpg")

dst = cv2.Canny(img, 60, 200)

cv2.imshow("img", img)
cv2.imshow("dst", dst)

key = cv2.waitKey(0)