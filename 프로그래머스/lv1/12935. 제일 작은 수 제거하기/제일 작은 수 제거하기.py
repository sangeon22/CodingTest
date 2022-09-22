def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        arr.append(-1)
        return arr
    
    else:
        return arr