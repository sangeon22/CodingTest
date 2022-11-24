import math

# # 소수 판별
# def prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

def solution(a, b):
    # 분모를 기약분수로 바꿔줌
    b //= math.gcd(a, b)

    # 소인수 분해
    i = 2
    while i <= b:
        if b % i == 0:
            b /= i
            if i not in (2, 5):
                return 2
        else:
            i += 1

    return 1