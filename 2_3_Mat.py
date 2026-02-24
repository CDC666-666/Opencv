import cv2
import numpy as np

#Mat的属性：dims, rows, cols, channels, size, type, depth, data

img = cv2.imread("/home/c/桌面/Opencv/test_1.jpg")
#浅拷贝
img2 = img
#深拷贝
img3 = img.copy()

img[10:100, 10:100] = [255, 255, 255]

#cv2.imshow("img", img)
#cv2.imshow("img2", img2)
#cv2.imshow("img3", img3)

print(img.shape)
print(img.size)
print(img.dtype)

img4 = np.zeros((480, 640, 3), np.uint8)   
b,g,r = cv2.split(img)
cv2.imshow("b", b)
cv2.imshow("img", img)

key = cv2.waitKey(0)
