t = int(input())

total_y = 0
total_k = 0

for i in range(t):
    for j in range(9):
        y, k = map(int, input().split())
        total_y += y
        total_k += k

    if total_y > total_k:
        print("Yonsei")
    elif total_y == total_k:
        print("Draw")
    else:
        print("Korea")
