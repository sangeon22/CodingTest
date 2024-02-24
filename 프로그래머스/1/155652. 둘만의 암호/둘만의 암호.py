def solution(s, skip, index):
    answer = ''

    # skip 문자 제외한 a-z
    arr = [i for i in "abcdefghijklmnopqrstuvwxyz" if i not in skip]

    for i in s:
        # index 만큼 건너뛴 target_index, arr길이를 넘어서면 다시 앞부터 순회
        target_idx = arr.index(i) + index
        target_idx %= len(arr)
        answer += arr[target_idx]

    return answer