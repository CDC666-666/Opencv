import cv2
import numpy as np

#图像轮廓提取：findContours(image, mode, method, offset) 返回轮廓和层次结构
#mode：轮廓提取模式，有四种：RETR_EXTERNAL=0（表示只检测外轮廓）, RETR_LIST=1（检测的轮廓不建立层级）, RETR_CCOMP（每层两级）, RETR_TREE（树形）
#method：轮廓逼近方法，有四种：CHAIN_APPROX_NONE（保存所有轮廓的点）, CHAIN_APPROX_SIMPLE（保存角点）, CHAIN_APPROX_TC89_L1, CHAIN_APPROX_TC89
#offset：轮廓坐标偏移量

#绘制轮廓：drawContours(image, contours, contourIdx, color, thickness)
#contourIdx：轮廓索引，-1表示绘制所有轮廓
img = cv2.imread("/home/c/桌面/Opencv/test_1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 1)

cv2.imshow("img", img)


key = cv2.waitKey(0)