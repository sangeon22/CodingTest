N = int(input())
nums = list(map(int, input().split()))
count = 0
for i in nums:
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                count += 1
            break
print(count)
