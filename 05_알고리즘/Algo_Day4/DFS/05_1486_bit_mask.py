import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N: 사람 수, B: 선반 높이
    N, B = map(int, input().split())
    # 점원들의 키 높이
    arr = list(map(int, input().split()))
    # 최종 결괏값 -> B를 넘는 값 중 가장 작은 값
    # 적절히 큰 기본값을 사용하자.
    result = 10000 * 20 + 1

    # 모든 경우의 수 (공집합 제외하고 처리)
    # for i in range(1, 1 << N):
    for i in range(1, 2**N):
        height = 0
        for j in range(N): # 0번부터 N번까지의 사람을 선택했는지 판별용
            # 각 부분 집합
            # i번째 경우에서 j번째 요소가 선택되었는지를 판별
            if i & (1 << j):
                height += arr[j]
        # 모든 요소에 대해서 i번째 경우의 수를 다 구했다면
        if height >= B:
            result = min(height, result)
    print(f'#{tc} {result - B}')
