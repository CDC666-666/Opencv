import cv2
import numpy as np

video_path = '/home/c/桌面/Opencv/video.avi'

cap = cv2.VideoCapture(video_path)

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

#形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

while True:
    ret, frame = cap.read()

    if(ret == 1):

        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#灰度
        blur = cv2.GaussianBlur(frame, (3 ,3), 5)#去燥(gaosi)
        mask = bgsubmog.apply(blur)#去背景

        #腐蚀
        erode = cv2.erode(mask, kernel)

        #膨胀
        dilate = cv2.dilate(erode, kernel, iterations = 1)

        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)

        cnts, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for(i, c) in enumerate(cnts):
            (x, y, w, h)= cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)

        cv2.imshow('video', frame)


    key = cv2.waitKey(10)
    if(key & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()

