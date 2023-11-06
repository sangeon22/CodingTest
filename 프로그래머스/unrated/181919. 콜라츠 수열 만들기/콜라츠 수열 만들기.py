def solution(n):
    li = []
    while True:
        li.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        
        if n == 1:
            li.append(n)
            return li
