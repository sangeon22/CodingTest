def solution(s, m, c):
    return ''.join([i for i in s][c-1::m])