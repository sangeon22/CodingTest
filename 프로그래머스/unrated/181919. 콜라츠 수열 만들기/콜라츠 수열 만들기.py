def solution(n):
    li = []
    while n != 1:
        li.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        
    li.append(n)
    return li
