import cv2 as cv
import numpy

blankImage = numpy.zeros((400,400,3),dtype=numpy.uint8)
# cv.imshow("Blank", blankImage)


blankImage[0:50,0:50] = 255,255,255





cv.imshow("Drawing Board", blankImage)
cv.waitKey(0)