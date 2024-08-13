import cv2 as cv

# Read an image
img = cv.imread("img1.jpg")
cv.imshow("window", img)
cv.waitKey(0)
