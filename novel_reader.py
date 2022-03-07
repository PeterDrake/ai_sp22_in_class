from collections import defaultdict

with open('moby.txt') as f:
    lines = f.readlines()


def f():
    return 0


counts = defaultdict(f)

for line in lines:
    for c in line:
        c = c.lower()
        counts[c] += 1

for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(f'{letter}: {counts[letter]}')
