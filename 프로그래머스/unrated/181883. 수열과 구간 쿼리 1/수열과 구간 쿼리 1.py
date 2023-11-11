def solution(arr1, arr2):
    for i, j in arr2:
        for k in range(len(arr1)):
            if i <= k <= j:
                arr1[k] += 1
    return arr1