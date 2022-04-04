import random


def sample():
    x = random.random()
    y = random.random()
    if x**2 + y**2 < 1:
        return 1
    return 0


def pi(n):
    darts = [sample() for x in range(n)]
    return 4 * (sum(darts) / n)
