import cv2
import numpy as np

#图像卷积：filter（src, ddepth, kernel, anchor, delta, borderType）
#方盒滤波：boxFilter（src, ddepth, ksize, anchor, normalize, borderType），如果kernel为None，则使用boxFilter
#均值滤波：blur（src, ksize, anchor, borderType）
#高斯滤波：GaussianBlur（src, ksize, sigmaX, sigmaY, borderType）对高斯噪声有很好的去除效果
#中值滤波：medianBlur（src, ksize）对胡椒盐噪声有很好的去除效果
#双边滤波：bilateralFilter（src, d, sigmaColor, sigmaSpace, borderType）可以保留边缘信息，并对边缘内区域进行平滑处理，但是速度慢,美颜
#卷积核：kernel
#矛点：anchor
#边界类型：borderType
img = cv2.imread("/home/c/桌面/Opencv/test_1.jpg")

#kernel = np.ones((5, 5), np.float32)/25
#dst = cv2.filter2D(img, -1, kernel)
#dst = cv2.blur(img, (5, 5))
#dst = cv2.GaussianBlur(img, (5, 5), sigmaX=1, sigmaY=1)
#dst = cv2.medianBlur(img, 33)
dst = cv2.bilateralFilter(img, 201, 75, 75)
cv2.imshow("img", img)
cv2.imshow("dst", dst)

key = cv2.waitKey(0)