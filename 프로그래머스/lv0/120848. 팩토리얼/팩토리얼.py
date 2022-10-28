def solution(n):
    total = 1
    for i in range(1, 12):
        total *= i
        if n < total:
            return i-1