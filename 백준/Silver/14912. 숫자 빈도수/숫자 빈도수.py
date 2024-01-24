from collections import Counter

n, d = map(int, input().split())

c = Counter("".join([str(i) for i in range(1, n + 1)]))
print(c[str(d)])
