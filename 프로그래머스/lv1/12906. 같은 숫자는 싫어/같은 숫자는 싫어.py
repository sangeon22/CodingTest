def solution(arr):
    answer = []
    pre = 1000001
    for i in arr:
        if i != pre: 
            answer.append(i)
            pre = i
    return answer