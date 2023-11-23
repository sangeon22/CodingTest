def solution(n, s, li):
    if n == 1:
        return li[:s[1]+1]
    elif n == 2:
        return li[s[0]:]
    elif n == 3:
        return li[s[0]:s[1]+1]
    elif n == 4:
        return li[s[0]:s[1]+1:s[2]]
