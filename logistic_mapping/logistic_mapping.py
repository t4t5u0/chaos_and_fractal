# ロジスティック写像

import argparse
import numpy as np
import matplotlib.pyplot as plt

# x_n+1 = ax_n(1-x_n)
# 初期条件
a = 3.853
x_0 = 0.1

# logistic_mapping
def logistic(a, x_0):
    x = [x_0]
    for _ in range(100):
        x.append(a * x[-1] * (1-x[-1]))
    return x

# 演算
x = logistic(a, x_0)

# リターンマップ
fig_1 = plt.figure()
ax_1 = fig_1.add_subplot(xlabel='x_n', ylabel='x_n+1', title='return map')
ax_1.plot(x[:len(x)-1], x[1:],ls='', marker='.')
fig_1.savefig(f'./logistic_mapping/return_map_{a}_{x_0}.png')
#plt.show()

# 時系列のグラフ
fig_2 = plt.figure()
ax_2 = fig_2.add_subplot(xlabel='n', ylabel='x_n', title='time_sereis')
ax_2.plot(x)
fig_2.savefig(f'./logistic_mapping/time_series_{a}_{x_0}.png')
#plt.show()

print('finish successfully')


