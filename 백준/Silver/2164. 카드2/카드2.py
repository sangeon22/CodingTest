from sys import stdin
from collections import deque

n = deque(range(1, int(stdin.readline()) + 1))

while n != 1:
    if len(n) == 1:
        break
    else:
        n.popleft()
        n.rotate(-1)

print(n[0])