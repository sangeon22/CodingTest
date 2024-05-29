import math


def solution(n, k):
    answer = 0
    # k 진수 변환 함수
    number = jinsu(n, k)

    # 변환된 수를 분리 후 소수 판별 함수
    prime_number_list = list(map(int, filter(None, number.split('0'))))
    for i in prime_number_list:
        if i == 1:
            continue
        if prime_number_check(i):
            answer += 1

    return answer


def jinsu(n, k):
    num = ''
    while n > 0:
        n, mod = divmod(n, k)
        num += str(mod)
    return num[::-1]


def prime_number_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# n = 437674
# k = 3
# # 기댓값 3

n = 110011
k = 10
# 기댓값 2
print(solution(n, k))
