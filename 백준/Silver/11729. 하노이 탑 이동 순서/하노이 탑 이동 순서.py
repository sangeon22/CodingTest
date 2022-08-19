from sys import stdin

N = int(stdin.readline())
total = (2 ** N) - 1


def hanoi(n, start, end, sub):
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, sub, end)
        print(start, end)
        hanoi(n - 1, sub, end, start)



print(total)
hanoi(N, 1, 3, 2)
