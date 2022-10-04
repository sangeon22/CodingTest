def solution(n):
    count = bin(n)[2:].count('1')
    for i in range(n+1,1000001):
        if count == bin(i)[2:].count('1'):
            return i