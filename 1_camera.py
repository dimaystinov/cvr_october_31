import cv2
from pprint import pprint

cap = cv2.VideoCapture(0)

while True:
    # ret - получилось ли достать кадр return code
    # frame - сам кадр
    ret, frame = cap.read()
    print(ret)
    for el in frame:
        for i in el:
            print(i,end='')
        print()

    # Название окна , сам кадр
    cv2.imshow('camera', frame)
    # Ожидать нажатия клавиши 1 мс
    cv2.waitKey(1)
    break
