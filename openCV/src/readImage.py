import cv2 as cv

img = cv.imread('/home/utgupta27/PycharmProjects/python-projects/openCV/images/butterfly.jpg')

print(img.shape)

cv.imshow("ImageView", img)
cv.waitKey(0)