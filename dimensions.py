import random
import numpy as np
import matplotlib.pyplot as plt


# def point(d):
#     return [random.random() for x in range(d)]
#
#
# def is_near_the_edge(p):
#     return any([x < 0.1 or x > 0.9 for x in p])
#
#
# def fraction(d):
#     return sum([is_near_the_edge(point(d)) for _ in range(10000)]) / 10000


def point(d):
    return np.random.random(d)


def is_near_the_edge(p):
    return np.any(np.logical_or(p < 0.1, p > 0.9))


def fraction(d):
    return np.sum([is_near_the_edge(point(d)) for _ in range(10000)]) / 10000


x = range(1, 21)
y = [fraction(d) for d in x]

plt.plot(x, y)
plt.show()
