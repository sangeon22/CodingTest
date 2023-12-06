def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(j in ["0","5"] for j in str(i)):
            answer.append(i)
            
    return [-1] if len(answer) == 0 else answer