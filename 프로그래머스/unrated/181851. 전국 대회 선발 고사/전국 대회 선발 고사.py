def solution(r, a):
    li = sorted([i for i in enumerate(r) if a[i[0]]], key = lambda x:x[1])
    return 10000 * li[0][0] + 100 * li[1][0] + li[2][0]
