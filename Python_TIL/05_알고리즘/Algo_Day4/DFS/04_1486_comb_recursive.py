# 04_1486_comb_recursive

import sys
sys.stdin = open('input.txt', 'r')

# def combination(arr, r):
#     acc = [] # 누적 결과값을 저장한 배열
#     if r == 1: # 선택할 요소가 1인 경우
#         return [[i] for i in arr]
#     for i in range(len(arr)):
#         elem = arr[i]
#         for rest in combination(arr[i+1:], r-1):
#             acc.append([elem] + rest)
#     return acc

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    # N: 사람 수, B: 선반 높이
    N, B = map(int, input().split())
    # 점원들의 키 높이
    arr = list(map(int, input().split()))
    # 최종 결괏값 -> B를 넘는 값 중 가장 작은 값
    # 적절히 큰 기본값을 사용하자.
    result = 10000 * 20 + 1

    # 완전 검색
    for r in range(1, N+1): # 1명부터 N명까지 선택
        # 전체 배열 arr에서 r명 선택한 조함
        for comb in combinations(arr, r):
            total_hieght = sum(comb)
            if total_hieght >= B:
                result = min(total_hieght, result)
    print(f'#{tc} {result - B}')