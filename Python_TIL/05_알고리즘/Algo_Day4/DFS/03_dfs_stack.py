V = 7
E = 8

edfe_data=[
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 4],
    [3, 5],
    [4, 5],
    [5, 6]
]

adj_matrix = [[0]*V for _ in range(V)]

for idx in range(E):
    S, E = edfe_data[idx]
    adj_matrix[S][E] = 1
    adj_matrix[E][S] = 1

visited = [False] * V

def dfs(now):
    # stack -> 다음 조사 대상 후보군을 모두 여기에 삽입
    stack = [now]
    visited[now] = True
    # stack에 값이 있는 동안 계속 탐색
    while stack:
        # 가장 마지막에 들어온 값을 pop해서 조사 대상으로 지정
        now = stack.pop()
        print(now, end=' ') # 현재 방문한 대상 출력
        for next in range(V):
            if adj_matrix[now][next] and not visited[next]:
                stack.append(next)
                visited[next] = True

for idx in range(V):
    # 한 번 이라도 방문한 적이 있다면
    if visited[idx]:
        continue
    else:
        dfs(0)
