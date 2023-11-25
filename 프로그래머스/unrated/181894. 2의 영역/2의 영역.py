def solution(arr):
    if 2 not in arr:
        return [-1]
    start = arr.index(2)
    reversed_arr = arr[::-1]
    end = len(arr) - reversed_arr.index(2) - 1

    return arr[start: end + 1]

arr = [1, 2, 1, 4, 5, 2, 9]
print(solution(arr))

