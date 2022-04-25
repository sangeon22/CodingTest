T = int(input())

# 6 12 10 => 402
# 1 1 1 => 101
# 1 8 7 => 107
# 30 50 72 => 1203
# 6 12 6 => 601
# 6 12 12 => 101 201 301 401 501 601 102 ... 602
# 층, 각 층의 방 수, 몇번째 손님
for i in range(T):
    H, W, N = map(int, input().split())
    if H > 1:
        if N % H == 0:
            # 5 10 5 => 501
            # 5 10 10 => 502
            # 5 10 6 => 102
            floor = H
            room_num = N // H
        else:
            floor = N % H
            room_num = N // H + 1
    elif H == 1:
        floor = 1
        room_num = N
    print(floor * 100 + room_num)
