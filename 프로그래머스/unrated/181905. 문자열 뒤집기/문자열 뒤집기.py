def solution(x, s, e):
    return x[0:s] + x[s:e+1][-1::-1] + x[e+1:]