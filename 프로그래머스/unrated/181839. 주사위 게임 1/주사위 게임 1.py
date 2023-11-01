def solution(a, b):
    if a % 2 == 0 :
        if b % 2 == 0:
            return abs(a-b)
        else:
            return (a+b) * 2
    else:
        if b % 2 == 0:
            return (a+b) * 2
        else:
            return a**2 + b**2
