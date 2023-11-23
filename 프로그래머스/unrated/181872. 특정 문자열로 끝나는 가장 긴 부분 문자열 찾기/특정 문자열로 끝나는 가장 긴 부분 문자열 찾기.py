def solution(s, p):
    a = s[::-1]
    b = p[::-1]
    for i in range(len(s)):
        if a[i] == b[0]:
            if a[i:i+len(b)] == b:
                return a[i::][::-1]