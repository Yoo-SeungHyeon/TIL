import sys

sys.stdin = open('input.txt', 'r')


# DFS로 모든 조합 찾기
def DFS(result, target, n, history):
    if n == 0:
        result.add(target)
        return

    if (target, n) in history:
        return
    else:
        history.add((target, n))

    target_list = list(target)
    for i in range(len(target_list)):
        for j in range(i + 1, len(target_list)):
            target_list[i], target_list[j] = target_list[j], target_list[i]
            DFS(result, ''.join(target_list), n - 1, history)
    return result


T = int(input())
for tc in range(1, T + 1):
    num, chan = input().split()
    num_size = len(num)
    chance = int(chan)
    result = set()
    history = set()
    results = DFS(result, num, chance, history)
    print(f'#{tc} {max(results)}')
