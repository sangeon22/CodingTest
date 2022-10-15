def solution(num, k):
    li = list(map(int, str(num)))
    if k in li:
        return li.index(k)+1
    else:
        return -1