from sys import stdin

n = list(map(str, stdin.readline()))
n.sort(reverse=True)
for i in n:
    print(i, end="")