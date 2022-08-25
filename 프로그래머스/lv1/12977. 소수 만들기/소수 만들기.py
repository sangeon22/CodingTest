import math
import itertools


def solution(nums):
    answer = 0
    a = []
    data = itertools.combinations(nums, 3)
    for i in data:
        a.append(sum(i))

    for i in a:
        if prime(i):
            answer += 1
    return answer


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True