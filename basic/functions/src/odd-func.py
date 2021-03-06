#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = x**3

fig, ax = plt.subplots()
fig.set_label('$x^3$')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.plot(x, y, 'r-', label='$ f(x) = x^3$ ')
plt.legend(loc='upper left')
fig.savefig('../out/odd.png')
