def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def combine(f, ls):
    return f(ls[0], ls[1])


def make_adder(n):
    def adder(x):
        return x + n
    return adder

def identity(x):
    return x

def negative(x):
    return -x

def largest(f, *ns):
    result = ns[0]
    for n in ns:
        if f(n) > f(result):
            result = n
    return result

def tricky(a, *b, c):
    print(a)
    print(b)
    print(c)


def tricky2(a, b, c):
    print(a)
    print(b)
    print(c)

def t3(**kwargs):
    print(kwargs)
