import sys

sys.stdin = open('sample_input.txt', 'r')


# 모든 경우의 수를 all_result에 저장
def dfs(grid, i, j, r, result, all_results):
    if not r:
        all_results.add(result)
        return

    # 방향 가중치 (상, 하, 좌, 우) = (x-1, x+1, y-1, y+1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 4가지 경우(상하좌우) 중 조건(격자판을 벗어나는지)에 부합하면 동작
    for di, dj in directions:
        ni, nj = i + di, j + dj  # 이동한 좌표
        if 0 <= ni < 4 and 0 <= nj < 4:  # 격자판 범위 확인
            dfs(grid, ni, nj, r - 1, result + grid[ni][nj], all_results)

    return all_results


T = int(input())
for tc in range(1, T + 1):
    grid = []
    for _ in range(4):
        grid.append(input().split())
    all = set() # 중복 방지를 위해 집합 사용
    for i in range(4):
        for j in range(4):
            dfs(grid, i, j, 7, '', all) # 참조값으로 적용돼서 따로 return이 없어도 됨
    # 갯수만 출력
    print(f'#{tc} {len(all)}')
