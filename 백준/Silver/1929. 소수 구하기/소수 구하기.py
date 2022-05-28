import math


def prime_num(num):
    if num == 1:
        return False

    n = int(math.sqrt(num))
    for i in range(2, n+1):
        if num % i == 0:
            return False
    return True


m, n = map(int, input().split())

for i in range(m, n + 1):
    if prime_num(i):
        print(i)
