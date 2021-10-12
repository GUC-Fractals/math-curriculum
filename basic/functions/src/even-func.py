#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = x**2

fig, ax = plt.subplots()
fig.set_label('$x^2$')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.plot(x, y, 'r-', label='$ f(x) = x^2$ ')
plt.legend(loc='upper left')
fig.savefig('../out/graphs.png')
