from sys import stdin

N, k = map(int, stdin.readline().split(" "))

li = list(map(int, stdin.readline().split(" ")))

li.sort(reverse=True)
# print(sorted(li, reverse=True))
print(li[k-1])
