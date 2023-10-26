def solution(s, pat):
    return 1 if pat in ''.join(['B' if i == 'A' else 'A' for i in s]) else 0
