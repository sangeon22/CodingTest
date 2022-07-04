from sys import stdin

t = int(stdin.readline())

for i in range(t):
    a = list(stdin.readline().split())
    li = []

    for j in a:
        li.append(j[::-1])

    print(*li)