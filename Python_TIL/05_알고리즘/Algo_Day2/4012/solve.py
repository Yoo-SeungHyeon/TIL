# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# from itertools import combinations
#
# def taste_sum(matrix, args):
#     result = 0
#     for a in args:
#         for b in args:
#             result += matrix[a][b]
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     table = []
#     for _ in range(N):
#         table.append(list(map(int, input().split())))
#     # 조합을 통해 가능한 경우의 수 계산
#     recipe_list = list(range(N))
#     all_comb = combinations(recipe_list, N//2)
#     pair_comb = []
#     not_duple = []
#     for comb in all_comb:
#         if comb not in not_duple:
#             pair = tuple(set(recipe_list)- set(comb))
#             pair_comb.append((comb, pair))
#             not_duple.append(comb)
#             not_duple.append(pair)
#     result = 999999999
#     for pair1, pair2 in pair_comb:
#         sum1 = taste_sum(table, pair1)
#         sum2 = taste_sum(table, pair2)
#         if result >= abs(sum1 - sum2):
#             result = abs(sum1 - sum2)
#     print(f'#{tc} {result}')

import sys
sys.stdin = open('sample_input.txt', 'r')

def taste_sum(matrix, group):
    total_taste = 0
    for i in group:
        for j in group:
            total_taste += matrix[i][j]
    return total_taste

def solve(N, matrix):
    min_diff = float('inf')

    def find_combinations(index, current_group):
        nonlocal min_diff

        if len(current_group) == N // 2:
            other_group = [i for i in range(N) if i not in current_group]
            diff = abs(taste_sum(matrix, current_group) - taste_sum(matrix, other_group))
            min_diff = min(min_diff, diff)
            return

        if index == N:
            return

        # 현재 재료를 선택하는 경우
        find_combinations(index + 1, current_group + [index])
        # 현재 재료를 선택하지 않는 경우
        find_combinations(index + 1, current_group)

    find_combinations(0, [])
    return min_diff


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    result = solve(N, matrix)
    print(f'#{tc} {result}')
