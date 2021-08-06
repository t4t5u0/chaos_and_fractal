from typing import TypedDict
import numpy as np
from numba import jit
import matplotlib.pyplot as plt


class Param(TypedDict):
    x: float
    y: float
    w: float
    h: float


@jit
def mandelbrot(Re: float, Im: float, max_iter: int) -> int:
    c = complex(Re, Im)
    z = 0.0j

    for i in range(max_iter):
        z = z*z + c
        if(z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter


def calc(param: Param) -> tuple[np.ndarray, Param]:
    columns = 8000
    rows = 4000
    result = np.zeros([rows, columns])
    # ここを領域ごとに分割して、あとでくっつける処理を書きたい
    for row_index, Re in enumerate(np.linspace(param['x'], param['y'], num=rows)):
        for column_index, Im in enumerate(np.linspace(param['w'], param['h'], num=columns)):
            result[row_index, column_index] = mandelbrot(Re, Im, 100)
    return result, param


def plot(result: tuple[np.ndarray, Param]):
    result, param = result
    plt.figure(dpi=500)
    plt.imshow(result.T, cmap='bone', interpolation='bilinear',
               extent=[-0.759, -0.757, 0.0755, 0.077])
    plt.xticks()
    plt.yticks()
    # plt.tick_params(length=0)
    # plt.show()
    plt.savefig(f"{param['x']}_{param['y']}_mandelbrot.png")


def main():
    params: list[Param] = [{'x': 1, 'y': 1, 'w': 1, 'h': 1}]
    for param in params:
        print(param)
        plot(calc(param))


if __name__ == '__main__':
    main()
