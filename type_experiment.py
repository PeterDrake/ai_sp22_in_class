# The Python type hierarchy is surprisingly hard to find a diagram of. I'm working out which
# classes extend which abstract base classes.

from collections.abc import *

abcs = [Container, Hashable, Iterable, Iterator, Generator, Collection, Sequence, MutableSequence, Set, MutableSet,
        Mapping, MutableMapping]


def g():
    for i in range(10):
        yield i


items = [g(), 1, 1.0, 1+2j, True, 'hello', set(), dict(), [], (1,), range(1), zip(), (i for i in [1, 2]), object(), None]

for i in items:
    classes = [str(c)[str(c).rfind('.')+1:-2] for c in abcs if isinstance(i, c)]
    print(type(i), classes)

