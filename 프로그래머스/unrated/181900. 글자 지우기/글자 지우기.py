def solution(s, idx):
    return ''.join([s[i] for i in range(len(s)) if i not in idx])