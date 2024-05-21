def solution(bandage, health, attacks):
    # 마지막 공격 시간, 최대 체력, 연속 성공 시간, 현재 시간이 공격 시간인지 여부, 데미지
    last_attack_time = attacks[-1][0]
    max_health = health
    use_time = 0
    attack_bool = False
    attack_damage = 0

    # 1초부터 마지막 공격까지 진행
    for i in range(1, last_attack_time + 1):
        # 공격 시간 체크
        for j in attacks:
            if j[0] > i:
                break

            # 공격 시간일 경우, 데미지 및 공격 여부 저장
            if j[0] == i:
                attack_damage = j[1]
                attack_bool = True

        # 공격 여부가 True
        if attack_bool:
            health -= attack_damage
            use_time = 0
            attack_bool = False
            attack_damage = 0

            # 체력이 0 이하인 경우
            if health <= 0:
                return -1

        # 공격 여부가 False
        else:
            use_time += 1
            # 이미 최대 체력이 아닌 경우만 체력 ++;
            if health != max_health:
                # 치유될 체력이 최대 체력 보다 높은 경우, 현재 체력을 최대 체력
                if health + bandage[1] >= max_health:
                    health = max_health
                else:
                    health += bandage[1]
                    if use_time == bandage[0]:
                        health += bandage[2]
                        use_time = 0

    return health


# # bandage는[시전 시간, 초당 회복량, 추가 회복량]
# bandage = [5, 1, 5]
# # attacks[i]는 [공격 시간, 피해량]
# attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
# health = 30
# 기댓값 5

bandage = [1, 10, 10]
health = 5
attacks = [[97, 4], [99, 4]]
# 기댓값 1
print(solution(bandage, health, attacks))
