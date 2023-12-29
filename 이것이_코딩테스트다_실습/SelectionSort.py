'''
선택 정렬: 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞 데이터와 바꾸는 것 반복
'''

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        # 선형 탐색으로 가장 작은 원소 탐색
        if arr[min_idx] > arr[j]:
            min_idx = j
    # 맨 앞 데이터와 가장 작은 데이터를 바꿈
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)

'''
선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
N + (N-1) + (N-2) + ... + 2 => (N**2 + N -2) / 2 => O(N**2)
'''