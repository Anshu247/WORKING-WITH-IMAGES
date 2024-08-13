import cv2 as cv

img = cv.imread("img1.jpg")
img_crop = img[0:300, 0:300]

cv.imwrite("fruits_crop.jpg", img_crop)

cv.imshow("window", img_crop)
cv.waitKey(0)
