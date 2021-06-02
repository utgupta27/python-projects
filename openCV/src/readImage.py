import cv2 as cv

picture = cv.imread("images/butterfly.jpg")

print(picture.shape)
cv.imshow("ImageView", picture)
cv.waitKey(0)