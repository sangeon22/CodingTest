def solution(arr, idx):
    try:
        return len(arr[:idx]) + arr[idx:].index(1)
    except:
        return -1