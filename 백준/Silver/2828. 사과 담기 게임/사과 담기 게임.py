n, m = map(int, input().split())
answer = 0
start = 0
end = m
# direction = "right"
# idx = [i for i in range(0, m)] if m >= 2 else [0]
# for i in range(int(input())):
#     target = int(input()) - 1
#     while target not in idx:
#         # 벽에 닿으면 방향 전환
#         if idx[-1] == n - 1:
#             direction = "left"
#         elif idx[0] == 0 and i != 0:
#             direction = "right"
#
#         if direction == "right":
#             idx = list(map(lambda x: x + 1, idx))
#         else:
#             idx = list(map(lambda x: x - 1, idx))

for _ in range(int(input())):
    target = int(input())

    if target < start:
        answer += start - target
        start = target
        end = target + m - 1
    elif target > end:
        answer += target - end
        end = target
        start = end - m + 1

print(answer)
