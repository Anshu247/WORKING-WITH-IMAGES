import cv2 as cv

img = cv.imread("img1.jpg")
cv.imshow("window_1", img)

print(img.shape)

img_resize = cv.resize(img, (300, 300))

cv.imshow("window_2", img_resize)
print(img_resize.shape)

cv.waitKey(0)
