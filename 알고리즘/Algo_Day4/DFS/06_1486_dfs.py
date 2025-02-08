# 04_1486_comb_recursive

import sys
sys.stdin = open('input.txt', 'r')

# idx: 조사 대상의 index
# count: 조사한 대상들의 수
# total: 그 대상들의 키의 합
def dfs(idx, count, total):
    global result
    # total이 B보다 크면 # 조사 종료 조건
    if total >= B: # 유망성을 충족하는 조건
        # 둘 중 더 작은 값
        result = min(total, result)
        return
    # 추가 조사 종료 조건
    # 더 이상 선택할 사람이 없거나,
    # 이미 모든 인원을 조사한 경우 종료
    if idx == N or count == N:
        return
    # 현재 index 번째 사람을 조사 대상에 추가하고 다음 사람 조사
    # 다음 사람 조사를 위해 index 1증가
    # 현재 사람을 선택했으니 count 1증가
    # 현재 사람의 키만큼을 total 추가
    dfs(idx+1, count+1, total + arr[idx])
    # 현재 번째 사람을 total에 추가하지 않고, 넘어감
    # 따라서 count는 1 증가하지 않음
    # 따라서 total도 증가하지 않음
    # 단, 다음 사람을 조사 하러 갈 것이기 때문에 idx만 1증가함.
    dfs(idx+1, count, total)

T = int(input())
for tc in range(1, T+1):
    # N: 사람 수, B: 선반 높이
    N, B = map(int, input().split())
    # 점원들의 키 높이
    arr = list(map(int, input().split()))
    # 최종 결괏값 -> B를 넘는 값 중 가장 작은 값
    # 적절히 큰 기본값을 사용하자.
    result = 10000 * 20 + 1

    dfs(0, 0, 0)

    print(f'#{tc} {result - B}')