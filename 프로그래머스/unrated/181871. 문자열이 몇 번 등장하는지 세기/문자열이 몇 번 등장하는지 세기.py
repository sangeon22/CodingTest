def solution(s, p):
    answer = 0
    for i in range(len(s)):
        if s[i] == p[0]:
            if p == s[i:i+len(p)]:
                answer += 1

    return answer
