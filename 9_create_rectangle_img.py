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
    elif event == 4:
        fx = x
        fy = y
        flag = False
        cv.rectangle(img_res, pt1=(ix, iy), pt2=(x, y), color=(0, 0, 0), thickness=1)
        cropped = img_res[iy:fy, ix:fx]
        cv.imshow("new_window", cropped)
        cv.waitKey(0)
        cv.imwrite("img2.jpg", cropped)
        print("Cropped Image Saved Successfully")


cv.namedWindow(winname="window")
cv.setMouseCallback("window", draw)
img = cv.imread("img1.jpg")
img_res = cv.resize(img, (300, 300))

while True:
    cv.imshow("window", img_res)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cv.destroyAllWindows()
