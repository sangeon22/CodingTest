def solution(n):
    li = []
    for i in range(500):
        if i % 3 != 0 and "3" not in str(i):
            li.append(i)
            if len(li) == n:
                return i
