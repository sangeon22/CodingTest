import sys


def f(num):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if num > 2:
        for i in range(3, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print("{} {}".format(zero[num], one[num]))


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    f(n)