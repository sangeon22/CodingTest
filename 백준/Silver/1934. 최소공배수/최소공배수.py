import math

def lcm(a, b):
    return int(a * b / math.gcd(a,b))


t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))
