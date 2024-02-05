n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
while l >= min(arr):
    for i in arr:
        if l >= i:
            arr.remove(i)
            l += 1
    if not arr:
        break
print(l)
