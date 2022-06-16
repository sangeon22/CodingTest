from sys import stdin
from itertools import combinations
n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
total = 0

# for i in range(0, len(a)):
#     for j in range(i + 1, len(a)):
#         for k in range(j + 1, len(a)):
#             sum_value = a[i] + a[j] + a[k]
#             if sum_value <= m:
#                 total = max(total, sum_value)
# print(total)

total = [sum(i) for i in combinations(a, 3) if sum(i) <= m]
print(max(total))