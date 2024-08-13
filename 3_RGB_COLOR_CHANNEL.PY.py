import cv2 as cv
import numpy as np

img = cv.imread("fruits_crop.jpg")

img_blue = img[:, :, 0]
img_green = img[:, :, 1]
img_red = img[:, :, 2]

new_img = np.hstack((img_blue, img_green, img_red))

cv.imshow("window", new_img)
cv.waitKey(0)
