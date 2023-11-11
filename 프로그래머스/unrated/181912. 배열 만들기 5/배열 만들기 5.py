def solution(arr, k, s, l):
    return [int(i[s:s+l]) for i in arr if int(i[s:s+l]) > k]