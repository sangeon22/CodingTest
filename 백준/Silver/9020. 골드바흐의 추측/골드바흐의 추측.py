# 1. 소수 판별 함수 만들고
# 2. n의 중간 값을 소수로 판별?
# 3. 소수가 아니면 -1, +1 격차 벌리면서 소수로 구성된 합 찾기?

from sys import stdin


def prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


T = int(stdin.readline())
for i in range(T):
    n = int(stdin.readline())

    a = int(n / 2)
    b = int(n / 2)

    for _ in range(int(n / 2)):
        if prime(a) is True and prime(b) is True:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
