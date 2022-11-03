import math

def prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0:
            if prime(i):
                answer.append(i)

    return answer