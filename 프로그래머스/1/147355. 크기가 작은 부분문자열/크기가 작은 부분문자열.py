def solution(t, p):
    li = [t[i:i+len(p)] for i in range(len(t)) if len(t[i:i+len(p)]) == len(p)]
    return sum([1 for i in li if int(i) <= int(p)]) 