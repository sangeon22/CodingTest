def solution(arr, k):
    li = []
    for i in arr:
        if i not in li:
            li.append(i)
    
    if len(li) < k:
        for i in range(k-len(li)):
            li.append(-1)
        return li
    else:
        return li[:k]
        
    