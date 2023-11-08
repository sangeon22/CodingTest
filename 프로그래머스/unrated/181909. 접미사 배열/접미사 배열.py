def solution(s):
    return sorted([s[i::1] for i in range(len(s))])