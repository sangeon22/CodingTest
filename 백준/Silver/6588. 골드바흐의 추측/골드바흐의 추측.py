from sys import stdin
import math


def prime(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


while True:
    n = int(stdin.readline())

    if n == 0:
        break

    for i in range(3, n + 1):
        if prime(i):
            if prime(n - i):
                print("{} = {} + {}".format(n, i, n - i))
                break