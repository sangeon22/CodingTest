from sys import stdin
import math
# 최대공약수 = gcd
# 최소공배수 = lcm

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#         return a

n, s = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))

temp = []
for i in a:
    temp.append(abs(s - i))

result = temp[0]
for i in temp:
    result = math.gcd(result, i)

print(result)
