import math


def lcm(x, y):
    return int(x * y / math.gcd(x, y))


def solution(arr):
    # lcm = (a * b) / math.gcd(a,b)
    answer = arr[0]
    for i in range(len(arr) - 1):
        if i != len(arr) - 1:
            answer = lcm(answer, arr[i + 1])

    return answer
