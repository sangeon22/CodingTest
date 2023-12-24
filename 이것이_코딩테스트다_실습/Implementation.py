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

# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성하라. 예를 들어 1을 입력했을 때
#
# 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다
# 00시 00분 03초
# 00시 13분 30초
#
# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다
# 00시 02분 55초
# 01시 27분 45초
#
# 시간제한 : 2초
# 메모리제한 : 128MB
# [입력]
# 첫째 줄에 정수 N이 입력된다.(0<=N<=23)
#
# [출력]
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
#
# [입력 예시]
# 5
#
# [출력 예시]
# 11475

# (1차 - 해설 안보고 혼자 풀기) => 그냥 중첩반복 완전탐색으로 품
n = int(input())
hh, mm, ss = 0, 0, 0
answer = 0
my_start_time = time.time()

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if str(i).find("3") > -1 or str(j).find("3") > -1 or str(k).find("3") > -1:
                answer += 1
print(answer)
my_end_time = time.time()
print(my_end_time - my_start_time)

# # (2차 - 책 풀이) => 하루는 86,400초 파이썬은 1초에 2천만번으로 생각하면 약소한 수 => 역시 완전탐색
h = int(input())

book_start_time = time.time()
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
book_end_time = time.time()
print(book_end_time - book_start_time)
# 10
# 19350
# 0.028920412063598633
# 10
# 19350
# 0.029920101165771484


# 행복 왕국의 왕실 정원은 체스판과 같은 8 × 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서있다.
# 나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다
# 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있다
#
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
#
# 이처럼 8 × 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는
# 프로그램을 작성하라. 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는
# a 부터 h로 표현한다
#
# c2에 있을 때 이동할 수 있는 경우의 수는 6가지이다
# a1에 있을 때 이동할 수 있는 경우의 수는 2가지이다
#
# 시간제한 : 1초
# 메모리제한 : 128MB
#
# [입력]
# 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1 처럼 열과 행으로 이뤄진다.
#
# [출력]
# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
#
# [입력 예시]
# a1
#
# [출력 예시]
# 2

# (1차 - 해설 안보고 혼자 풀기) => 8개 경우만 체크하면 될꺼같아서 반복문 안쓰고 풀었다
n = input()
my_start_time = time.time()
x = [int(n[1]), ord(n[0])-96]
answer = 0
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# print([x[0] + 2, chr(x[1] + 1 + 96)])
# print([x[0] + 2, chr(x[1] - 1 + 96)])
# print([x[0] - 2, chr(x[1] + 1 + 96)])
# print([x[0] - 2, chr(x[1] - 1 + 96)])
#
# # 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# print([x[0] + 1, chr(x[1] + 2 + 96)])
# print([x[0] - 1, chr(x[1] + 2 + 96)])
# print([x[0] + 1, chr(x[1] - 2 + 96)])
# print([x[0] - 1, chr(x[1] - 2 + 96)])

if 0 < x[0] + 2 < 9 and 0 < x[1] + 1 < 9:
    answer += 1
if 0 < x[0] + 2 < 9 and 0 < x[1] - 1 < 9:
    answer += 1
if 0 < x[0] - 2 < 9 and 0 < x[1] + 1 < 9:
    answer += 1
if 0 < x[0] - 2 < 9 and 0 < x[1] - 1 < 9:
    answer += 1
if 0 < x[0] + 1 < 9 and 0 < x[1] + 2 < 9:
    answer += 1
if 0 < x[0] - 1 < 9 and 0 < x[1] + 2 < 9:
    answer += 1
if 0 < x[0] + 1 < 9 and 0 < x[1] - 2 < 9:
    answer += 1
if 0 < x[0] - 1 < 9 and 0 < x[1] - 2 < 9:
    answer += 1
print(answer)
my_end_time = time.time()
print(my_end_time - my_start_time)

# (2차 - 책 풀이) => 내 풀이랑 전반적으로 비슷했다 ord 사용해서 보기 편하게 치환하고 경우의 수 체크, 그런데 steps처럼 벡터 방향을 미리 정의하고 사용하니 가독성 측면에서는 더 좋은 듯, 경우의 수가 너무 적어서 for 사용하든 안하든 속도차이 없을 듯
data = input()
book_start_time = time.time()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1
print(result)
book_end_time = time.time()
print(book_end_time - book_start_time)


# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
#
# [입력]
# 첫째 줄에 하나의 문자열 S가 주어집니다. (1<=S의 길이<=10,000)
#
# [출력]
# 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

# (1차 - 해설 안보고 혼자 풀기)
s = input()
answer = ''.join(sorted([i for i in s if i.isalpha()])) + str(sum([int(i) for i in s if i.isdigit()]))
print(answer)

# (2차 - 책 풀이)
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))