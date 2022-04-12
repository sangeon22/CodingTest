n = int(input())
hansu = 0

for i in range(1, n + 1):
    if i <= 99:
        hansu += 1

    else:
        num = list(map(int, str(i)))
        if num[0] - num[1] == num[1] - num[2]:
            hansu += 1
print(hansu)