from sys import stdin
from math import factorial

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


N = int(stdin.readline())
a = str(factorial(N))
count = 0

for i in a[-1::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)
