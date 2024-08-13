import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((400, 400, 3), np.uint8)

# square
sqr = cv.rectangle(img, pt1=(100, 100), pt2=(300, 300), color=(255, 0, 0), thickness=-1)
cv.imshow("window", sqr)

# circle
cir = cv.circle(img, center=(100, 400), radius=50, color=(0, 0, 255), thickness=3)
cv.imshow("window", cir)

# line
#
lin = cv.line(img, pt1=(0, 0), pt2=(512, 512), color=(0, 255, 0), thickness=2)
cv.imshow("window", lin)

# rectangle
rec = cv.rectangle(img, (100, 50), (400, 150), (198, 131, 56), thickness=-1)
cv.imshow("window", rec)

# text
txt = cv.putText(img, org=(100, 100), fontScale=4, color=(0, 255, 255), thickness=2, lineType=cv.LINE_AA, text="Hello", fontFace=cv.FONT_ITALIC)
cv.imshow("window", txt)

cv.waitKey(0)
