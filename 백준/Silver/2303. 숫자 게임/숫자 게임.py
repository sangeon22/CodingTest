from itertools import combinations

n = int(input())
player = []
answer = {str(i):0 for i in range(1, n+1)}
for _ in range(n):
    player.append(map(int, input().split()))

for i in range(len(player)):
    arr = list(map(sum, combinations(player[i], 3)))
    answer[str(i + 1)] = int(max([str(result)[-1] for result in arr]))

print(max([key for key, value in answer.items() if value == max(answer.values())]))

# [17, 16, 21, 16, 21, 20, 14, 19, 18, 18]
# [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# [8, 7, 15, 7, 15, 14, 8, 16, 15, 15]
