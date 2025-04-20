import sys

sys.stdin = open('sample_input.txt', 'r')

def check(arr, x):
    # x-1 이라는 값이 핵심
    core = x-1
    for idx in arr:
        # 너무 끝쪽에 있으면 경사로 설치 못함
        if core <= idx < len(arr) - core:
            pass
    pass


T = int(input())
for tc in range(1):
    N, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for arr in data:
        print(check())
