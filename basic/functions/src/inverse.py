#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.dpi"] = 140
x = np.linspace(2, 10, 1000000)


def f(input):
    return math.sqrt(input - 2) + 3


vfunc = np.vectorize(f)
y = vfunc(x)

fig, ax = plt.subplots()

ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

ax.set_aspect("equal")
plt.xlim(-3, 10)
plt.ylim(-1, 10)

ax.plot(x, y, 'r-', linewidth=2, label='$\sqrt{x-2} + 3$', alpha=0.6)

ax.set_title('Horizental Line text')
ax.legend(loc='best')

fig.savefig('../out/inverse.png')
