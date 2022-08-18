from sys import stdin


def total(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return total(n - 1) + total(n - 2) + total(n - 3)


T = int(stdin.readline())

for i in range(T):
    n = int(stdin.readline())
    print(total(n))
