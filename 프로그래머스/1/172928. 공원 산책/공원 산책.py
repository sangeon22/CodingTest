# 주석 일부 깜빡해서 추가 후 재커밋
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
        # 이동거리만큼 1씩 증가, 감소하다가 장애물(X)을 만나거나 맵(park)을 벗어나면 현재 좌표를 다시 원래 좔표로 돌리기 위한 원래좌표
        origin_x, origin_y = x, y
        
        # 방향, 이동 거리 추출
        item = i.split()
        direction = item[0]
        distance = int(item[1])
        
        for _ in range(distance):
            # 맵을 벗어나지 않고 장애물을 만나지 않는 경우, 방향으로 +-1칸 이동
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
