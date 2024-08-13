import cv2 as cv

img = cv.imread("img1.jpg")

# vertical flip
# img_flip = cv.flip(img,0)

# horizontal flip
img_flip = cv.flip(img,1)

# img_flip = cv.flip(img, -1)

cv.imshow("window", img_flip)
cv.waitKey(0)

