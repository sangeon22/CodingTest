import math

def solution(n):
    answer = 0
    if math.sqrt(n) % 1 != 0:
        return -1
    else:
        return (math.sqrt(n) + 1) ** 2 
