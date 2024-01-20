from itertools import combinations

arr = [int(input()) for _ in range(9)]
li = list(combinations(arr, 7))
for i in li:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
