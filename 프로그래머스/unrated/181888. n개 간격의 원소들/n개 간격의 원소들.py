def solution(num, n):
    return [num[i] for i in range(len(num)) if i % n == 0]