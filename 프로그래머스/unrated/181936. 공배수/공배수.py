def solution(number, n, m):
    # return 1 if number % (n*m) == 0 else 0 
    # number = 8, n = 8, m = 4
    return 1 if (number % n == 0) and (number % m == 0) else 0