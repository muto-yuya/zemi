#-*-coding: UTF-8-*-
import numpy as np
import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
width = 8
while True:
    ret, frame = cap.read()
    #frameを表示
    frame = np.array(frame)
    for i in range(frame.shape[1]):
        if (int(i%width))<6:
            frame[:,i,:] = np.zeros((frame.shape[0],3))
    cv2.imshow('camera capture', frame)

    #10msecキー入力待ち
    k = cv2.waitKey(10)
    #Escキーを押されたら終了
    if k == 27:
        break

#キャプチャを終了
cap.release()
cv2.destroyAllWindows()