# 머릿속에 있는 알고리즘을 소스코드로 변환하는 것

# 여행가 A는 N × N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 × 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다. 우리 앞에는 여행가 A가
# 이동할 계획이 적힌 계획서가 놓여 있다
#
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.
# 각 문자의 의미는 다음과 같다
# L: 왼쪽으로 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위로 한 칸 이동
# D: 아래로 한 칸 이동
#
# 이때 여행가 A가 N × N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다
# 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시된다
# 다음은 N = 5인 지도와 계획이다
#
# 시간제한 : 2초
# 메모리제한 : 128MB
#
# [입력]
# 첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. (1<=N<=100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다. (1<=이동 횟수<=100)
#
# [출력]
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력
#
# 입력 예시
# 5
# R R R U D D
#
# 출력 예시
# 3 4
#
import time

# (1차 - 해설 안보고 혼자 풀기)
n = int(input())
plan = list(map(str, input().split()))
x, y = 0, 0

my_start_time = time.time()
for i in plan:
    if i == "L" and y > 0:
        y -= 1
    elif i == "R" and y < n-1:
        y += 1
    elif i == "U" and x < 0:
        x -= 1
    elif i == "D" and x < n-1:
        x += 1

print(x+1, y+1)
my_end_time = time.time()
print(f"1차 풀이 소요시간: {my_end_time - my_start_time}")

# 요구사항대로 충실히 구현
# 일련의 명령을 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로도 분류
# 시뮬레이션 유형, 구현 유형, 완전 탐색 유형은 서로 유사한 점이 많다

# (2차 - 책 풀이)
n = int(input())
plans = input().split()
x, y = 1, 1

book_start_time = time.time()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
book_end_time = time.time()
print(f"2차 풀이 소요시간: {book_end_time - book_start_time}")
