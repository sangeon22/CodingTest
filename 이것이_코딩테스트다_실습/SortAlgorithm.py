'''
정렬 알고리즘     | 평균 시간복잡도 | 공간복잡도   |                             특징                           |                  사용법
선택정렬         |  O(N**2)     |    O(N)    |       아이디어 매우 간단                                      |     처리되지 않은 가장 작은 데이터를 맨 앞 데이터와 바꾸는 것 반복
삽입정렬         |  O(N**2)     |    O(N)    |      데이터가 거의 정렬되어 있을 때 가장 빠름                   |     처리되지 않은 데이터를 골라 적적한 위치 삽입반복
퀵정렬          |  O(NlogN)    |    O(N)    |      대부분의 경우에 가장 적합, 충분히 빠름                     |    기준보다 큰 데이터와 작은데이터를 바꿈, 재귀
계수정렬        |   O(N+k)     |    O(N+K)  |      데이터의 크기가 한정되어 있는 경우에만 사용 가능, 매우 빠름   |    인덱스로 등장 횟수에 따라 반복

대부분 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)
'''

'''
동빈이는 두 개의 배열 A와 B를 가지고 있다.
두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다

동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데,
바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다

동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야한다

N, K, 그리고 배열 A와 B의 정보가 주어졌을 때,
최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하라

예를 들어 N = 5, K = 3이고, 배열 A와 B가 다음과 같다고 해보자
배열 A = [1, 2, 5, 4, 3]
배열 B = [5, 5, 6, 6, 5]
이 경우, 다음과 같이 세 번의 연산을 수행할 수 있다

연산 1) 배열 A의 원소 '1'과 배열 B의 원소 '6'을 바꾸기
연산 2) 배열 A의 원소 '2'와 배열 B의 원소 '6'을 바꾸기
연산 3) 배열 A의 원소 '3'과 배열 B의 원소 '5'를 바꾸기

세 번의 연산 이후 배열 A와 배열 B의 상태는 다음과 같이 구성될 것이다
배열 A = [6, 6, 5, 4, 5]
배열 B = [3, 5, 1, 2, 5]
이때 배열 A의 모든 원소의 합은 26이 되며, 이보다 더 합을 크게 만들 수는 없다

[입력]
첫 번째 줄: N, K 가 공백으로 구분되어 입력 (1 <= N <= 100,000, 0 <= K <= N)
두 번째 줄: 배열 A의 원소들이 공백으로 구분되어 입력 (원소 a < 10,000,000인 자연수)
세 번째 줄: 배열 B의 원소들이 공백으로 구분되어 입력 (원소 b < 10,000,000인 자연수)

[출력]
최대 K번 바꿔치기 연산을 수행해서 가장 최대의 합을 갖는 A의 모든 원소 값의 합을 출력

[입력 예시]
5 3
1 2 5 4 3
5 5 6 6 5

[출력 예시]
26
'''
import datetime

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 풀이 안보고 내 방식대로 풀어보기 => 풀이보니까 b가 더 작은 숫자로 구성되어 있는 상황을 생각못했다
my_start_time = datetime.datetime.now()
print(sum(sorted(b, reverse=True)[0:k] + sorted(a)[k:]))
my_end_time = datetime.datetime.now()
time_difference = my_end_time - my_start_time
print(f"시간 차이: {time_difference.total_seconds():.10f} 초")

# 책 풀이(위 input 입력 방식은 같음)
book_start_time = datetime.datetime.now()
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
book_end_time = datetime.datetime.now()
time_difference = book_end_time - book_start_time
print(f"시간 차이: {time_difference.total_seconds():.10f} 초")