def solution(players, callings):
    # 단순 반복은 시간초과 뜰 것 같아서 추월 수 만큼 인덱스 조정으로 바꿨으나 실패
    # cnt = 0
    # runner = ""
    # for i in callings:
    #     cnt += 1
    #     if i != runner:
    #         runner = i
    #     elif i == runner:
    #         now_idx = players.index(runner) - cnt
    #         back_runner = players[now_idx:]
    #         back_runner.remove(runner)
    #         players = players[:now_idx] + [runner] + back_runner
    #         runner = ""
    #         cnt = 0
    # return players

    # 플레이어의 현재 위치를 저장하는 리스트
    positions = list(range(len(players)))

    # 플레이어 이름을 키로, 그들의 위치 인덱스를 값으로 하는 사전 생성
    dic = {player: i for i, player in enumerate(players)}

    for i in callings:
        x = dic[i]
        positions[x], positions[x - 1] = positions[x - 1], positions[x]
        dic[players[positions[x]]] = x
        dic[i] = x - 1

    return [players[x] for x in positions]