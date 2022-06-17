from sys import stdin

n = int(stdin.readline())
a = []
for i in range(n):
    a.append(int(stdin.readline()))

a.sort()
for i in a:
    print(i)