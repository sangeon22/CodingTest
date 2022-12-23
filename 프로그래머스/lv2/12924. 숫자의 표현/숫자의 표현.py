def solution(n):
    total = 0
    count = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            total += j
            if total == n:
                count += 1
                break
            if total > n:
                break
        total = 0
    return count