import cv2
import numpy as np

#图像二值化：threshold（src, thresh, maxval, type, dst）
#thresh：阈值
#maxval：当像素值超过阈值（或者小于阈值，取决于type），所赋予的值
#type：有三种阈值类型：THRESH_BINARY, THRESH_BINARY_INV, THRESH_TRUNC

#自适应阈值：adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
#adaptiveMethod：指定计算阈值的方法，有两种：ADAPTIVE_THRESH_MEAN_C和ADAPTIVE_THRESH_GAUSSIAN_C
#blockSize：用来计算阈值的区域大小，必须是正数和奇数
#C：阈值计算方法的参数，一般情况下是一个常数

img = cv2.imread("/home/c/桌面/Opencv/test_1.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
thresh1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)

cv2.imshow("img", img)
cv2.imshow("img1", img1)
cv2.imshow("thresh", thresh)
cv2.imshow("thresh1", thresh1)

key = cv2.waitKey(0)