def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    if not answer:
        answer.append(-1)
    
    answer.sort()
    return answer