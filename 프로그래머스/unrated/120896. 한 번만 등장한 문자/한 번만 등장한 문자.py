def solution(s):
    return ''.join(sorted([i for i in s if list(s).count(i) == 1]))