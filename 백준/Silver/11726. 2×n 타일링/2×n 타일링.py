import sys

input = sys.stdin.readline

n = int(input())
li = [0, 1, 2]

for i in range(3, n + 1):
    li.append((li[i - 1] + li[i - 2]) % 10007)

print(li[n])