from sys import stdin

n = int(stdin.readline())
li = []

for i in range(n):
    x, y = stdin.readline().split()
    li.append([int(x), y])

li.sort(key=lambda x: x[0])

for i in li:
    print(*i)
