'''
다이나믹 프로그래밍(동적 계획법, dp): 메모리를 적절히 사용하여 수행 시간 효율성으로 비약적으로 향상 시키는 방법
- 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장 -> 다시 계산 X
- 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운, 바텀업)

문제가 다음 조건을 만족할 때 다이나믹 프로그래밍 사용가능
1. 최적 부분 구조
    큰 문제를 작은 문제로 나눌 수 있고 작은 문제의 답을 모아 큰 문제를 해결
2. 중복되는 부분 문제
    동일한 작은 문제를 반복적으로 해결
'''

'''
피보나치 수열
1, 1, 2, 3, 5, 8, 13, 21 ...
점화식 : an = an-1 + an-2
'''


def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))


# 단순 재귀로 피보나치 수열을 계산하면 지수 시간 복잡도를 가지게 되고 수가 커지면 기하급수적으로 커짐
# 중복 부분 문제가 많음(피보나치를 트리로 만들어보면 예로 f(2)가 엄청 많음) => 중복 부분 문제를 미리 메모리에 기록
# 피보나치 수열은 위의 다이나믹 프로그래밍 조건 2가지를 만족
# 하향식(탑다운)에서 사용되는 메모이제이션(한 번 계산한 결과를 메모리 공간에 메모) 캐싱이라고도 함


# 탑다운 방식 dp => 재귀
def fibo_dp_top_down(x):
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면
    d[x] = fibo_dp_top_down(x - 1) + fibo_dp_top_down(x - 2)
    return d[x]


# 메모이제이션
d = [0] * 100
print(fibo_dp_top_down(99))

# 바텀업 방식 dp => 반복문
d1 = [0] * 100
d1[1] = 1
d1[2] = 1
n = 99

for i in range(3, n + 1):
    d1[i] = d1[i - 1] + d1[i - 2]
print(d1[n])

'''
다이나믹 프로그래밍과 분할 정복(퀵 정렬) 모두 최적 부분 구조를 가질 때 사용
1. 최적 부분 구조
    큰 문제를 작은 문제로 나눌 수 있고 작은 문제의 답을 모아 큰 문제를 해결
    
그러나 dp와 분할정복 차이점은
2. 중복되는 부분 문제
    동일한 작은 문제를 반복적으로 해결

퀵정렬에서 피벗을 통해 분할이 이뤄지고 피벗을 다시 처리하는 문제는 호출되지 않음
문제를 보고 어떤 알고리즘을 사용할 수 있는지 파악하는 것이 중요!!
완전탐색 -> 재귀 -> 코드 개선 겸 탑다운 방식 db 적용
'''

'''
난이도 2/3
풀이시간 30분
시간제한 1초
메모리 제한 128MB

개미전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다.
메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져 있다.
각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다.
이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.
따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
예를 들어 식량창고 4개가 다음과 같이 존재한다고 가정하자.

{1, 3, 1, 5}
이때 개미 전사는 두 번째 식량창고와 네 번째 식량창고를 선택했을 때 최댓값인 총 8개의 식량을 빼앗을 수 있다.
개미 전사는 식량창고가 이렇게 일직선상일 때 최대한 많은 식량을 얻기를 원한다.

개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 식량창고의 개수 N이 주어진다. (3<=N<=100)
둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다. (0<=K<=1,000)

[출력]
첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.

[입력 예시]
4
1 3 1 5

[출력 예시]
8
'''

n = int(input())
k = list(map(int, input().split()))
d = [0] * n
d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    # 한칸 전 값 / 두칸 전 값 + 현재 값
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])

'''
정수 X가 주어질때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.

1) X가 5로 나누어떨어지면, 5로 나눈다.

2) X가 3으로 나누어 떨어지면, 3으로 나눈다.

3) X가 2로 나누어 떨어지면, 2로 나눈다.

4) X에서 1을 뺀다.

정수 X가 주어졌을때, 연산 4개를 적절히 사용해서 1을 만들어야한다. 이 연산을 사용하는 횟수의 최솟값을 출력해라.

X = 26일 경우
1. 26 - 1 = 25
2. 25 /5 = 5
3. 5 / 5 = 1

[입력]
첫째 줄에 정수 X이 주어진다. (1<=X<=30,000)

[출력]
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

[입력 예시]
26

[출력 예시]
3
'''
x = int(input())
d = [0] * 30001

for i in range(2, x + 1):
    # 1을 빼는 경우
    d[i] = d[i - 1] + 1

    # 2로 나누는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    # 3으로 나누는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    # 5로 나누는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])


'''
N가지 종류의 화폐가 있다.
이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.

[입력 조건]
첫째 줄에 N,M이 주어진다(1<= N <= 100, 1<= M <= 10,000)
이후의 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.

[출력 조건]
첫째 줄에 경우의 수 X를 출력한다.
불가능할 때는 -1을 출력한다.

[입력 예시]
2 15
2
3

[출력 예시]
5
'''

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0
for i in range(n):
    for j in range(arr[i], m + 1):
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])


'''
n × m 크기의 금광이 있다.
금광은 1 × 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다.
맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라

만약 다음과 같이 3 x 4 크기의 금광이 존재한다고 가정합시다.

  1 3 3 2
  2 1 4 1
  0 6 4 7

가장 왼쪽 위의 위치를 (1, 1), 가장 오른쪽 아래의 위치를 (n, m)이라고 할 때,

위 예시에서는 (2, 1) → (3, 2) → (3, 3) → (3, 4)의 위치로 이동하면 총 19만큼의 금을 채굴할 수 있으며, 이때의 값이 최댓값입니다.

[입력 조건]
첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)
매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20)
둘째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (1 <= 각 위치에 매장된 금의 개수 <= 100)

[출력 조건]
테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다.
각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.

[입력 예시]
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

[출력 예시]
19
16
'''

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    d = []
    idx = 0

    for _ in range(n):
        d.append(arr[idx: idx + m])
        idx += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = d[i - 1][j - 1]

            if i == n - 1:
                left_down = 0
            else:
                left_down = d[i + 1][j - 1]

            left = d[i][j - 1]
            d[i][j] = d[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, d[i][m - 1])

    print(result)

'''
N명의 병사가 무작위로 나열되어 있다.
각 병사는 특정한 값의 전투력을 보유하고 있으며, 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 한다.
다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다.
또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다.
그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶다.

[입력 조건]
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 2,000) 둘째 줄에 각 병사의 전투력이 공백을 기준으로 구분되어 차례대로 주어진다. 각 병사의 전투력은 10,000,000보다 작거나 같은 자연수이다.

[출력 조건]
첫째 줄에 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외해야 하는 병사의 수를 출력한다.

[입력 예시]
7
15 11 4 8 5 2 4

[출력 예시]
2
'''
# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 사용
# d[i] = arr[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + 1)
print(n - max(d))