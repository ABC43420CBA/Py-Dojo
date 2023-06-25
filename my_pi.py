
from random import random

N = 1000

n = 0
for i in range(N):
    x = random()
    y = random()

    z = x*x + y*y
    if z <= 1.0:
        n = n + 1

pi = 4 * (n / N)
print(f'经过{N}轮的丢豆子，统计计算得出pi={round(pi,2)}')

for k in range(4):
    N = 10000 * 10**k

    n = 0
    for i in range(N):
        x = random()
        y = random()

        z = x*x + y*y
        if z <= 1.0:
            n = n + 1

    pi = 4 * (n / N)
    print(f'经过{N}轮的丢豆子，统计计算得出pi={round(pi,2)}')