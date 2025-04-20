import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

# 최종 결과값
result = -1 # 문제에서 요구하는 값을 넣으면 된다.

# 함수 이름을 DFS, BFS로 정의하는건 권장하지 않음.
# 함수의 이름은 정확한 용도로 작성하자.

get_road_move_time()