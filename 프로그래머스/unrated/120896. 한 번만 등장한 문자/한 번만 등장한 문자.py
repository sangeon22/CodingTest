def solution(s):
    return ''.join(sorted([i for i in s if s.count(i) == 1]))