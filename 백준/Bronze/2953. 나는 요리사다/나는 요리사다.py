a = [sum(list(map(int, input().split()))) for i in range(5)]
print(a.index(max(a)) + 1, max(a))
