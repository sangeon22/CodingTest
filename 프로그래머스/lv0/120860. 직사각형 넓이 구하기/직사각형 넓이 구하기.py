def solution(dots):
    a = max(dots, key=lambda x:x[0])[0] - min(dots, key=lambda x:x[0])[0]
    b = max(dots, key=lambda x:x[1])[1] - min(dots, key=lambda x:x[1])[1]
    return a*b