import random
from statistics import mean
from math import exp

def random01string(n=200):
    return ''.join([random.choice(('0', '1')) for _ in range(n)])


def population(m=1000, n=200):
    return [random01string(n) for _ in range(m)]


def fitness(individual, target):
    return exp(sum([a == b for a, b in zip(individual, target)]))


def mutate(individual):
    def opposite(a):
        if a == '0':
            return '1'
        return '0'
    r = 1 / len(individual)
    return ''.join(opposite(a) if random.random() < r else a for a in individual)


def cross(a, b):
    point = random.randint(0, len(a))
    return a[:point] + b[point:]


def generation(pop, target):
    """
    Returns the next generation.
    """
    f = [fitness(i, target) for i in pop]
    # result = random.choices(pop, f, k=len(pop))
    result = [cross(random.choices(pop, f)[0], random.choices(pop, f)[0]) for _ in range(len(pop))]
    # return result
    return [mutate(i) for i in result]


t = random01string()
p = population()

for i in range(100):
    f = [fitness(i, t) for i in p]
    print(i, max(f), mean(f))
    p = generation(p, t)

