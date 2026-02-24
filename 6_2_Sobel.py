import cv2
import numpy as np

#Sobel算子：Sobel（src, ddepth, dx, dy, ksize, scale, delta, borderType）先向x方向求导，再向y方向求导
#Scharr算子：Scharr（src, ddepth, dx, dy, scale, delta, borderType）只能处理3*3的卷积核，求导方向只能是x或y
#拉普拉斯算子：Laplacian（src, ddepth, ksize, scale, delta, borderType）

img = cv2.imread("/home/c/桌面/Opencv/test_1.jpg")

#sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
#sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

#dst = cv2.add(sobelx, sobely)
#dst = cv2.Scharr(img, cv2.CV_64F, 1, 0)
dst = cv2.Laplacian(img, cv2.CV_64F,5)

cv2.imshow("img", img)
cv2.imshow("dst", dst)

key = cv2.waitKey(0)