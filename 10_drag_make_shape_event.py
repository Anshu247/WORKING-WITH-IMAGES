import cv2 as cv
import numpy as np

flag = False
ix = -1
iy = -1


def draw(event, x, y, flags, params):
    global flag, ix, iy
    if event == 1:
        flag = True
        ix = x
        iy = y
    elif event == 0:
        if flag:
            cv.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=-1)
    elif event == 4:
        flag = False
        cv.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=-1)


cv.namedWindow(winname="window")
cv.setMouseCallback("window", draw)
img = np.zeros((400, 400, 3))

while True:
    cv.imshow("window", img)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cv.destroyAllWindows()
