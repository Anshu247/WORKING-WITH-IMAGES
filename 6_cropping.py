import cv2 as cv

img = cv.imread("img1.jpg")
cv.imshow("window_1", img)

img_crop = img[0:300, 0:300]
cv.imshow("window_2", img_crop)

cv.waitKey(0)
