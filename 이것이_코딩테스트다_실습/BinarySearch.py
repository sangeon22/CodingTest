'''
순차 탐색: 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인
이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터 탐색 O(logN)
'''


def binary_search_iterate(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    # 중간점 보다 타겟이 작은 경우, 왼쪽으로 범위 이전
    elif arr[mid] > target:
        return binary_search_iterate(arr, target, start, mid - 1)
    # 중간점 보다 타겟이 큰 경우, 오른쪽으로 범위 이전
    elif arr[mid] < target:
        return binary_search_iterate(arr, target, mid + 1, end)


def binary_search_recursive(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
result1 = binary_search_iterate(arr, target, 0, n - 1)
if result1 is None:
    print("원소 존재X")
else:
    print(result1 + 1)

result2 = binary_search_recursive(arr, target, 0, n - 1)
if result2 is None:
    print("원소 존재X")
else:
    print(result2 + 1)

# 파이썬 이진 탐색 라이브러리
# bisect_left(arr, x): 정렬된 순서를 유지하며, 배열 arr에 x를 삽입할 가장 왼쪽 인덱스 반환
# bisect_right(arr, x): 정렬된 순서를 유지하며, 배열 arr에 x를 삽입할 가장 오른쪽 인덱스 반환
from bisect import bisect_left, bisect_right

arr = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(arr, x))
print(bisect_right(arr, x))


# 값이 특정 범위에 속하는 데이터 개수 구하기
def count_by_range(arr1, left, right):
    left_idx = bisect_left(arr1, left)
    right_idx = bisect_right(arr1, right)
    return right_idx - left_idx


arr1 = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(arr1, 4, 4))
print(count_by_range(arr1, -1, 3))


# 파라메트릭 서치
# 최적화 문제를 결정(yes || no) 문제로 바꾸어 해결하는 기법
# ex) 특정 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제 => 이진 탐색 이용