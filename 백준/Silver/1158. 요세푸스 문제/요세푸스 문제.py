from sys import stdin

n, k = map(int, stdin.readline().split())

li = []
result = []
idx = 0

for i in range(1, n + 1):
    li.append(i)

for i in range(n):
    idx += k - 1
    if idx >= len(li):
        idx %= len(li)

    result.append(str(li.pop(idx)))

print("<", ", ".join(result), ">", sep="")