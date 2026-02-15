import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('/home/cdc/桌面/Python/opencv/test_1.jpg')

cv2.imshow('img', img)

key = cv2.waitKey(0)
if(key & 0xFF== ord('q')):
  print(11)
  cv2.destroyAllWindows()