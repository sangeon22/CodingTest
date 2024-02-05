n = int(input())
arr = list(map(int, input().split()))
print(max(arr) + (sum(arr) - max(arr)) / 2)
