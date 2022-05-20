a = list(input())
sum = 10

for i in range(1, len(a)):
    if a[i] == a[i-1]:
        sum += 5
    elif a[i] != a[i-1]:
        sum += 10

print(sum)
