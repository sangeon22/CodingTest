def solution(s, q):
    s = list(s)
    for i in q:
        if i[0] != 0:
            s[i[0]:i[1]+1] = s[i[1]:i[0]-1:-1]
        else:
            s[i[0]:i[1]+1] = s[i[1]::-1]
    return ''.join(s)
