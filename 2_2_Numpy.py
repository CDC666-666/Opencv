import cv2
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)    

#(行，列，通道)
b = np.zeros(( 2, 3, 3), np.uint8)
print(b)

c = np.ones(( 2, 3, 3), np.uint8)
print(c)

d = np.full(( 2, 3, 3), 127, np.uint8)
print(d)

e = np.identity(3)
print(e)

f = np.eye(4,7,k=2 )
print(f)

img = cv2.imread('/home/c/桌面/Opencv/test_1.jpg')

#检索与修改像素
img = np.zeros((480, 640, 3), np.uint8)

print(img[100,100])
roi = img[100:200, 200:300]
roi[:] = [255, 255, 255]

count = 0
while count < 200:
    img[count,200] = (0, 0, 255)
    count += 1

cv2.imshow('img',img)

key = cv2.waitKey(0)
if(key & 0xFF== ord('q')):
    cv2.destroyAllWindows()

#ROI（y1：y2,x1:x2）

