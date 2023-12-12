def solution(t, p):
    answer = 0
    li = []
    for i in range(len(t)):
        if len(t[i:i+len(p)]) == len(p):
            li.append(t[i:i+len(p)])
    
    for i in li:
        if int(i) <= int(p):
            answer += 1
    return answer 