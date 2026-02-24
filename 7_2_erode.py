import cv2
import numpy as np

#获得卷积核：getStructuringElement(shape, ksize, anchor)
#shape：指定结构元素的形状，有三种：MORPH_RECT, MORPH_CROSS, MORPH_ELLIPSE
#腐蚀膨胀：erode(src, kernel, iterations) dilate(src, kernel, iterations)

#开操作：morphologyEx(src, cv2.MORPH_OPEN, kernel, iterations)
#闭操作：morphologyEx(src, cv2.MORPH_CLOSE, kernel, iterations)

#形态学梯度：morphologyEx(src, cv2.MORPH_GRADIENT, kernel, iterations)原图-腐蚀膨胀

#顶帽：morphologyEx(src, cv2.MORPH_TOPHAT, kernel, iterations)原图-开操作
#黑帽：morphologyEx(src, cv2.MORPH_BLACKHAT, kernel, iterations)开操作-原图
img=cv2.imread("/home/c/桌面/Opencv/test_1.jpg")

#kernel=np.ones((5,5),np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
#dst = cv2.erode(img, kernel, iterations = 10)
#dst1 = cv2.dilate(dst, kernel, iterations = 10)
#dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
dst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("erode", dst)
key = cv2.waitKey(0)