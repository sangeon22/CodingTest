from itertools import permutations

arr = [i for i in range(1, int(input()) + 1)]
for i in list(permutations(arr, len(arr))):
    print(*i)