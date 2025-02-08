import sys

sys.stdin = open('input.txt', 'r')


# target으로 만들 수 있는 순열을 전부 만든다.
# 만들어진 순열의 앞뒤에 1을 붙이고 이를 따라 배터리 소비량을 계산한다.
# min_battery 변수를 통해 최소값을 저장하고, 중간에 이 값을 넘기면 return한다.
def DFS(now, remain, battery):
    global result
    if not remain:
        battery += data[now][0]
        if result > battery:
            result = battery
            return

    if battery > result:
        return

    for i in range(len(remain)):
        select_idx = remain[i]
        value = data[now][select_idx]
        new_remain = remain[:i] + remain[i+1:]
        DFS(select_idx, new_remain, battery + value)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    target = list(range(1, N))
    # print(target)
    result = 100000000
    DFS(0, target, 0)
    print(f'#{tc} {result}')
