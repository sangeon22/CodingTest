def solution(n):
    li = []
    for i in range(n):
        temp = []
        for j in range(n):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        li.append(temp)
    return li
        
            