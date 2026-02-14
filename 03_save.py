import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('/home/cdc/桌面/Python/opencv/test_1.jpg')

while True:
   cv2.imshow('img', img)
   
   key = cv2.waitKey(0)
   if(key & 0xFF== ord('q')):
      print(123)
      break
   elif(key & 0xFF== ord('s')):
      print('save')
      cv2.imwrite('/home/cdc/桌面/C++/saved_image.jpg',img)
   else:
      print('other')