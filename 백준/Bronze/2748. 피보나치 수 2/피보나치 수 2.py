import sys

input = sys.stdin.readline

n = int(input())

li = [0, 1]

for i in range(2, n + 1):
    li.append(li[i - 1] + li[i - 2])

print(li[n])
