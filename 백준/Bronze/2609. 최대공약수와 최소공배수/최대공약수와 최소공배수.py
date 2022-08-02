from sys import stdin
import math


def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


a, b = map(int, stdin.readline().split())

# print(math.gcd(a, b))
print(gcd(a, b))
print(lcm(a, b))
