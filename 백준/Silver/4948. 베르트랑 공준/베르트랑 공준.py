# 시간 초과
# import math
# import sys
#
# def prime_num(num):
#     if num == 1:
#         return False
#
#     a = int(math.sqrt(num))
#     for i in range(2, a + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# while True:
#     count = 0
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break
#
#     for i in range(n, 2 * n + 1):
#         if prime_num(i):
#             count += 1
#     print(count)


num = []

for i in range(2, 246913):
    cnt = 0

    for p in range(2, int(i**0.5)+1):
        if i % p == 0:
            cnt += 1
            break

    if cnt == 0:
        num.append(i)

while True:
    n = int(input())
    res = 0

    if n == 0:
        break

    for i in num:
        if n < i <= 2*n:
            res += 1

    print(res)