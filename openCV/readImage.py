import cv2
import numpy
from matplotlib import pyplot

img = cv2.imread("/home/utgupta27/Pictures/pp.jpeg",cv2.IMREAD_COLOR)

image =  cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT)
# cv2.imshow('image',image)
# cv2.waitKey()

pyplot.imshow(image,'gray')
pyplot.show()