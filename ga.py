import random


def random01string(n=200):
    return ''.join([random.choice(('0', '1')) for _ in range(n)])

