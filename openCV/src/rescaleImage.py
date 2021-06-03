import cv2 as cv

def resizeImage(img,scale = 0.75):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    return cv.resize(img,(width, height),interpolation=cv.INTER_AREA)


img = cv.imread("/home/utgupta27/PycharmProjects/python-projects/openCV/images/butterfly.jpg")

img = resizeImage(img)
cv.imshow('Resized Image',img)
cv.waitKey(0)
cv.destroyAllWindows()
