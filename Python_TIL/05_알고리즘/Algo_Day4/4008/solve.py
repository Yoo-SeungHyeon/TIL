# import sys
#
# sys.stdin = open('sample_input.txt', 'r')
#
# from itertools import permutations
#
#
# def sum_oper(result, num, oper):
#     if oper == '+':
#         return result + num
#     elif oper == '-':
#         return result - num
#     elif oper == '*':
#         return result * num
#     elif oper == '/':
#         if result < 0:
#             return result // num + 1
#         else:
#             return result // num
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     plus, minus, multi, div = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     operator_list = ['+'] * plus + ['-'] * minus + ['*'] * multi + ['/'] * div
#     all_perm = permutations(operator_list, len(operator_list))
#     min_result, max_result = 100000000, -100000000
#     for perm in all_perm:
#         result = nums[0]
#         for i in range(1, N):
#             result = sum_oper(result, nums[i], perm[i - 1])
#         min_result = min(min_result, result)
#     print(f'#{tc} {max_result - min_result}')
#         max_result = max(max_result, result)


import sys

sys.stdin = open('sample_input.txt', 'r')

def dfs(depth, result, plus, minus, multi, div):
    global max_result, min_result

    # basic part. N번 반복했으면 결과 출력. 아니면 while문의 조건으로 연산자의 합을 써도 될 듯
    if depth == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if plus:
        dfs(depth + 1, result + nums[depth], plus - 1, minus, multi, div)
    if minus:
        dfs(depth + 1, result - nums[depth], plus, minus - 1, multi, div)
    if multi:
        dfs(depth + 1, result * nums[depth], plus, minus, multi - 1, div)
    if div:
        dfs(depth + 1, int(result / nums[depth]), plus, minus, multi, div - 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    plus, minus, multi, div = map(int, input().split())
    nums = list(map(int, input().split()))

    # 결과값 초기화
    max_result = -100000000
    min_result = 100000000

    # DFS 탐색 시작
    dfs(1, nums[0], plus, minus, multi, div)

    print(f'#{tc} {max_result - min_result}')
