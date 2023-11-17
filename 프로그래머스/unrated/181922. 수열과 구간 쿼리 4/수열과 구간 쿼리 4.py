def solution(arr, q):
    for s, e, k in q:
        for j in range(s,e+1):
            if j % k == 0:
                arr[j] += 1
    return arr