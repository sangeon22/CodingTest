'''
BFS(너비 우선 탐색) - 그래프에서 가가운 노드부터 우선 탐색하는 알고리즘, 큐 자료구조 사용

최단 경로 목적에서도 효과적

- 실행 순서
1. 시작 노드를 큐에 삽입 후 방문처리
2. 큐에서 노드를 꺼낸 후 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입 후 방문처리
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
'''
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

bfs(graph, 1, visited)

