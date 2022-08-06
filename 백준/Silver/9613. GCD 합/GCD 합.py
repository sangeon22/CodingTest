from sys import stdin
import math

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a


t = int(stdin.readline())

for i in range(t):
    li = list(map(int, stdin.readline().split(" ")))
    total = 0
    for j in range(1, len(li)):
        for k in range(j+1, len(li)):
            total += math.gcd(li[j], li[k])
    print(total)