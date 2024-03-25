def solution(park, routes):
    x, y = -1, -1

    # 공원 가로, 세로 길이
    park_w = len(park)
    park_h = len(park[0])

    # 시작점(S) 좌표 찾기
    for i in range(park_w):
        for j in range(park_h):
            if park[i][j] == 'S':
                x = i
                y = j
                break

    for i in routes:
        origin_x, origin_y = x, y
        item = i.split()
        direction = item[0]
        distance = int(item[1])
        for _ in range(distance):
            try:
                if direction == "N" and 0 <= x - 1 <= park_h - 1 and park[x - 1][y] != 'X':
                    x -= 1
                elif direction == "S" and 0 <= x + 1 <= park_h - 1 and park[x + 1][y] != 'X':
                    x += 1
                elif direction == "W" and 0 <= y - 1 <= park_w - 1 and park[x][y - 1] != 'X':
                    y -= 1
                elif direction == "E" and 0 <= y + 1 <= park_w - 1 and park[x][y + 1] != 'X':
                    y += 1
                else:
                    x = origin_x
                    y = origin_y
                    break
            except:
                x = origin_x
                y = origin_y

    return [x, y]