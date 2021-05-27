import numpy
from matplotlib import pyplot

x = numpy.arange(1,11,2)
y = [6,9,2,8,5]

x1 = numpy.arange(0,10,2)
y1 = [3,7,5,1,2]

pyplot.bar(x,y)
pyplot.bar(x1,y1)
pyplot.title('Bar Graph')
pyplot.xlabel('X - axis')
pyplot.ylabel('Y - axis')
pyplot.show()