## 점에서 레이저를 쏘는 느낌으로 그 방향으로 직선을 긋고, 교점을 찾아서 그 길이가 같은지를 확인

import sys
sys.stdin = open('sample_input.txt', 'r')

# 방향이 0 이면 y +=1
# 방향이 1 이면 y -=1
# 방향이 2 이면 x -=1
# 방향이 3 이면 x +=1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    elements = []
    for _ in range(N):
        elements.append(list(map(int, input().split())))

    # 중복없이 2쌍을 선택하는 모든 경우의 수
    for i in range(N):
        for j in range(i+1, N):
            way_i = elements[i][2]
            way_j = elements[j][2]
