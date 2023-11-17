def solution(arr, q):
    for i in q:
        a = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = a
    return arr