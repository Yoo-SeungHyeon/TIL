# 정점의 개수
V = 7
# 간선의 개수
E = 8
# 간선 정보
'''
그래프의 상황에 따라 간선 정보가 의미하는 바가 달라질 수 있다.
1. 무방향 그래프인 경우, 간선의 정보가 한 방향에 대해서 주어지더라도 
1-1. 양쪽 모두로 이어질 수 있음을 의미한다.
2. 유방향 그래프인 경우, 당연하게도 주어진 간선 정보가 끝
2-1. 주어진 정보 그대로 이해하면 된다.
시작정점 도착정점
   0      1   
   0      2   
   1      4   
      ...    
   5      6  
'''
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

def dfs(now):
    print(now)
    # 조회를 시작 했다. 그래서 now번째 방문을 표기
    visited[now] = True
    for next in range(V):
        # now -> next 이동 가능한지 인접 행렬로 체크
        # next 번째 방문한 적 없는지 체크
        if adj_matrix[now][next] and not visited[next]:
            dfs(next)

# 이차원 리스트나 딕셔너리로 표현하면 쉽다. 하지만 우리는 인접행렬을 사용해보자.
# 모든 노드의 개수만큼 만든다. V*V만큼 만들어야 한다.
adj_matrix = [[0]*V for _ in range(V)]

# 간선의 개수 만큼 간선 정보를 순회해서 인접행렬에 값을 적자.
for idx in range(E):
    S, E = edfe_data[idx]
    adj_matrix[S][E] = 1
    adj_matrix[E][S] = 1

# 인접행렬 확인
for i in range(V):
    print(adj_matrix[i])

# 방문 여부 확인
visited = [False] * V

# 모든 정점에 대해서 방문 가능한지 여부는 adj_matrix에 표기해둠.
# 그냥 모든 node에 대해서 순회를 하면됨.
for idx in range(V):
    # 한 번 이라도 방문한 적이 있다면
    if visited[idx]:
        continue
    else:
        dfs(0)