import numpy
from numba import autojit
import matplotlib.pyplot as plt

@autojit
def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j

    for i in range(max_iter):
        z = z*z + c
        if(z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter

columns = 8000
rows = 4000

result = numpy.zeros([rows, columns])
# ここを領域ごとに分割して、あとでくっつける処理を書きたい
for row_index, Re in enumerate(numpy.linspace(-0.759, -0.757, num=rows)):
    for column_index, Im in enumerate(numpy.linspace(0.0775, 0.0755, num=columns)):
        result[row_index, column_index] = mandelbrot(Re, Im , 100)

plt.figure(dpi=500)
plt.imshow(result.T, cmap='bone', interpolation='bilinear', extent=[-0.759, -0.757, 0.0755, 0.077])
plt.xticks()
plt.yticks()
#plt.tick_params(length=0)
#plt.show()
plt.savefig('mandelbrot.png')


'''
columns = 8000
rows = 4000

result = numpy.zeros([rows, columns])
# ここを領域ごとに分割して、あとでくっつける処理を書きたい
for row_index, Re in enumerate(numpy.linspace(-2., 1., num=rows)):
    for column_index, Im in enumerate(numpy.linspace(-1, 1, num=columns)):
        result[row_index, column_index] = mandelbrot(Re, Im , 100)

plt.figure(dpi=500)
plt.imshow(result.T, cmap='bone', interpolation='bilinear', extent=[-2, 1, -1, 1])
plt.xticks(color='None')
plt.yticks(color='None')
plt.tick_params(length=0)
#plt.show()
plt.savefig('mandelbrot.png')
'''