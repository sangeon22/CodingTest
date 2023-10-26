def solution(numbers, n):
    total = 0
    for i in numbers:
        total += i
        if total > n:
            return total
        
        