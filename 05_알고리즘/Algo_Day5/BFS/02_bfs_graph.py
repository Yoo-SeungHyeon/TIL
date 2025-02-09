from collections import deque

# 그래프 정보 입력 (어제(인접행렬 사용)와 다르게 인접 리스트로 진행)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['B', 'C', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['F'],
}

# 너비 우선 탐색 -> 방문 표시
visited = {key: False for key in graph}

result = [] # 스코프 개념으로 밖에 정의하고 사용 가능

def BFS(node):
    queue = deque(node)
    visited[node] = True
    while queue:
        now = queue.popleft()
        result.append(now)
        for child in graph[now]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True

# BFS('A')
# print(*result)

for node in graph:
    if node == 'F':
        BFS(node)
print(*result)