def solution(n):
    answer = [[0] * n for _ in range(n)]
    x = 0
    y = 0
    way = "r"

    count = 1
    while any(0 in i for i in answer):
        answer[x][y] = count

        if way == "r":
            if y + 1 == n or answer[x][y + 1] != 0:
                way = "d"
                x += 1
            else:
                y += 1

        elif way == "d":
            if x + 1 == n or answer[x + 1][y] != 0:
                way = "l"
                y -= 1
            else:
                x += 1

        elif way == "l":
            if answer[x][y - 1] != 0:
                way = "u"
                x -= 1
            else:
                y -= 1

        elif way == "u":
            if answer[x - 1][y] != 0:
                way = "r"
                y += 1
            else:
                x -= 1

        count += 1

    return answer