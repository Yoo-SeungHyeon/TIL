import sys

sys.stdin = open('sample_input.txt', 'r')


def dfs(grid, i, j, r, result, all_results):
    if r == 0:
        all_results.add(result)
        return

    # 가능한 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:  # 격자판 범위 확인
            dfs(grid, ni, nj, r - 1, result + grid[ni][nj], all_results)


T = int(input())
for tc in range(1, T + 1):
    grid = [input().split() for _ in range(4)]

    all_results = set()
    for i in range(4):
        for j in range(4):
            dfs(grid, i, j, 6, grid[i][j], all_results)  # 초기값을 미리 포함

    print(f'#{tc} {len(all_results)}')
