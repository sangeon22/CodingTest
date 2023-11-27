def solution(s):
    answer = []
    if "l" not in s and "r" not in s:
        return []
    for i in range(len(s)):
        if s[i] == "l":
            return s[:i]
        elif s[i] == "r":
            return s[i+1:]
