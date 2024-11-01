import cv2
cap = cv2.VideoCapture(0)
from random import randint
'''
list_example = [0, 1, 2, 3]
print(list_example[1:3])
exit()
'''
square_length = 100
while True:
    ret, frame = cap.read()
    print(frame.shape)
    height, width, _ = frame.shape

    frame[:, :, 0 ] = 255
    frame[:square_length, :square_length] = [randint(0, 255), randint(0, 255), randint(0, 255)]
    frame[height - square_length:, width - square_length:] = [randint(0,255), randint(0,255), randint(0,255)]
    frame[:square_length, width - square_length:] = [randint(0,255), randint(0,255), randint(0,255)]
    frame[height - square_length:, :square_length] = [randint(0,255), randint(0,255), randint(0,255)]
    frame[height // 2 - square_length // 2: height // 2 + square_length // 2, width // 2 - square_length // 2:width // 2 + square_length // 2] = [randint(0,255), randint(0,255), randint(0,255)]

    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    print(key)
    if key == ord(' '):
        break

#cv2.destroy_all_windows
cv2.destroyAllWindows()
cap.release()

