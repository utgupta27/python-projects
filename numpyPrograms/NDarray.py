import numpy
from matplotlib import pyplot

angles = numpy.arange(0,3*numpy.pi,1)
sinVal = numpy.sin(angles)
cosVal = numpy.cos(angles)

pyplot.subplot(2,1,1)
pyplot.title('Sine Graph')
# pyplot.xlabel("Angle/Radians")
pyplot.ylabel("Sin Values")
pyplot.plot(angles,sinVal)

pyplot.subplot(2,1,2)
pyplot.title('Cosine Graph')
pyplot.xlabel("Angle/Radians")
pyplot.ylabel("Cos Values")
pyplot.bar(angles,cosVal)

pyplot.show()