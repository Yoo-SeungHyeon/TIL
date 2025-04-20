import sys

sys.stdin = open('input2.txt', 'r')

from collections import deque

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]


def find_island(x, y):
    queue = deque([(x, y)])
    data[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y+ dy[k]
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 1:
                queue.append((nx, ny))
                data[nx][ny] = 0

N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
result = 0

# 시작지점은?
# 내가 가진 모든 데이터의 1에서 시작해봐야 함.
for x in range(N):
    for y in range(M):
        if data[x][y] == 1:
            find_island(x, y)
            result += 1

print(result)