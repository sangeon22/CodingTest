def solution(num, k):
    # li = list(map(int, str(num)))
    # if k in li:
    #     return li.index(k)+1
    # else:
    #     return -1
    a = str(num).find(str(k))+1
    return a if a != 0 else -1
