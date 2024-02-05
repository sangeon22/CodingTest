import math


def solution(number, limit, power):
    answer = 0
    weapon = [len(divisor(i)) for i in range(1, number + 1)]
    for i in weapon:
        if i > limit:
            answer += power
            continue
        answer += i

    return answer


def divisor(n):
    arr = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            arr.append(i)
            if n // i != i:
                arr.append(n // i)
    return arr