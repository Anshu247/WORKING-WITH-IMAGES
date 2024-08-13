import cv2 as cv

img = cv.imread("img1.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("window", img_gray)
cv.waitKey(0)

print(img_gray.shape)
