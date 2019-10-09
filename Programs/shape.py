import numpy
x = numpy.array([1, 2, 3, 4])
print(x.shape)

y = numpy.zeros((2, 3, 4))
print(y.shape)
print(y)
y.shape = (3, 8)
print(y)

i = 1
for i in range(19):
    print(i)
