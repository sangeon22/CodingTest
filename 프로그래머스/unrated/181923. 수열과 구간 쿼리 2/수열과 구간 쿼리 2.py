def solution(arr, q):
    answer = []
    for i in q:
        li = [j for j in arr[i[0]:i[1]+1] if j>i[2]]
        if len(li) > 0:
            answer.append(min(li))
        else:
            answer.append(-1)
    return answer