'''
DFS(깊이 우선 탐색)

- 실행 순서
1. 시작 노드를 스택에 삽입 후 방문처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면? 그 노드를 스택에 넣고 방문처리
                ...             인접한 노드가 없다면? 스택에서 최상단 노드를 꺼냄
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
'''


def dfs(graph, node, visited):
    visited[node] = True  # 방문처리
    print(node, end=" ")

    # 현재 (스택)최상단 노드와 연결된 노드들을 하나씩 확인
    for i in graph[node]:
        # 방문하지 않았다면? 재귀함수 호출
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],  # 대부분 1번 인덱스 부터 시작이니 0 인덱스 공백
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)