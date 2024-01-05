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


'''
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다.
오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기의 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
이걸 처리 안 해줘서 시간을 허비했다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1<=N<=1,000,000, 1<=M<=2,000,000,000)
둘째 줄에는 떡의 개별 높이가 주어진다.
떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

[입력]
4 6
19 15 10 17

[출력]
15
'''

# 혼자 풀어본 식 => 책 해설과 원리 비슷
def function(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        slice_list = list(map(lambda x: x - mid, arr))
        total = sum([i for i in slice_list if i > 0])
        if total == target:
            return mid
        elif total < target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(function(arr, m, 0, max(arr)))


'''
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
예를 들어 수열 {1,1,2,2,2,2,3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.

단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.

첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다. (1<=N<=1,000,000), (-10e9<=x<10e9)
둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다. (-10e9<=각 원소의 값<=10e9)

수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다.

[입력]
7 2

[출력]
1 1 2 2 2 2 3
'''

# 혼자 풀어본 식
# => 제약조건이 logN 복잡도고 라이브러리 사용이긴한데 답은 같지만 10e9처럼 큰 값이 들어오면 시간초과 떴을 수도 있다
# 알아보니 count, Counter 함수는 O(N)인데 가능할 것 같긴하다
n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(arr.count(x))

# 그래도 이진탐색을 활용해서 다시 한번 혼자 풀어본다.
from bisect import bisect_left, bisect_right


def count(arr, x):
    left_idx = bisect_left(arr, x)
    right_idx = bisect_right(arr, x)
    return right_idx - left_idx


result = count(arr, x)
print(-1 if result == 0 else result)
