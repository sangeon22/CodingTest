from sys import stdin


def pibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return pibo(num - 2) + pibo(num - 1)


n = int(stdin.readline())
print(pibo(n))