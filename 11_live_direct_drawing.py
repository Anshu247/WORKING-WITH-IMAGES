import cv2 as cv
import numpy as np


def draw(event, x, y, flags, params):
    if event == 1:
        cv.circle(img_res, center=(x, y), radius=50, color=(0, 0, 255), thickness=-1)


cv.namedWindow(winname="window")
cv.setMouseCallback("window", draw)
img = cv.imread("img1.jpg")
img_res = cv.resize(img, (400, 400))

while True:
    cv.imshow("window", img_res)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cv.destroyAllWindows()
