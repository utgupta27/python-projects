import numpy
from matplotlib import pyplot

data = numpy.array([20,50,10,87,88,19,94,54,24,11,89,65,79,75])
pyplot.hist(data,bins=[0,20,40,60,80,100])
pyplot.title('Histogram Data')
pyplot.show()