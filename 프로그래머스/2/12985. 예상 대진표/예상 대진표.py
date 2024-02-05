import math

# 깃
def solution(n, a, b):
    def binary(x, y, num):
        if (x > num // 2 and y > num // 2) or (x <= num // 2 and y <= num // 2):
            if abs(x - y) == 1:
                return 1

            if x - num // 2 < 1 or y - num // 2 < 1:
                return binary(x, y, num // 2)
            else:
                return binary(x - num // 2, y - num // 2, num // 2)
        else:
            return int(math.log(num, 2))

    return binary(a, b, n)
