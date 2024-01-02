'''
퀵정렬: 기준 데이터를 설정 -> 기준 보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
일반적으로 데이터의 특성과 관련없이 표준적으로 사용할 수 있는 정렬알고리즘 중 하나
일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘
병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준데이터(Pivot)으로 설정

평균의 경우, 너비 N * 높이 Nlog => O(NlogN)의 시간 복잡도를 가진다.
최악의 경우, O(N**2)의 시간 복잡도를 가진다. => 이미 정렬된 배열을 퀵정렬하는 경우
'''

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    # 왼쪽부터 pivot보다 큰 값 인덱스랑 오른쪽부터 pivot 작은 값 교환할 때, 엇갈리면 종료
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if (left > right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 이후, 왼쪽, 오른쪽을 재귀적으로 또 정렬
    quick(arr, start, right - 1)
    quick(arr, right + 1, end)


quick(arr, 0, len(arr) - 1)
print(arr)
