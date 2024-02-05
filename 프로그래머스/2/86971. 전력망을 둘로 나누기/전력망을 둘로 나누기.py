def solution(n, wires):
    answer = 9999

    for i in range(len(wires)):
        dic = {i: [] for i in range(1, n + 1)}
        w = wires.copy()
        pop_line = w.pop(i)
        group_a = []
        group_b = []

        # 제외된 간선의 노드를 각 그룹으로 분리
        for j in w:
            dic[j[0]].append(j[1])
            dic[j[1]].append(j[0])

        def divide(group, node):
            group.append(node)
            for connected_node in dic[node]:
                if connected_node not in group:
                    divide(group, connected_node)

        # group_a와 group_b 그룹에 연결된 모든 노드를 분리하기 위해 재귀 호출
        divide(group_a, pop_line[0])
        divide(group_b, pop_line[1])

        # 두 그룹의 크기 차이를 계산하고 최소값 갱신
        answer = min(abs(len(set(group_a)) - len(set(group_b))), answer)

    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
print(solution(n, wires))
