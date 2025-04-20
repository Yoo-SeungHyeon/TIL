import sys

sys.stdin = open("input.txt", 'r')


def find_last_max_index(target_list):
    target = max(target_list)
    for i in range(len(target_list) - 1, -1, -1):  # 뒤에서부터 탐색
        if target_list[i] == target:
            return i


def max_price(result, nl, change):
    if change == 0:
        result.extend(nl)
        return
    else:
        max_num_index = find_last_max_index(nl)
        if len(nl) == 2:
            max_price(result, nl[::-1], change - 1)
        else:
            if nl[max_num_index] == nl[0]:
                result.append(nl.pop(0))
                max_price(result, nl, change)
            else:
                nl[0], nl[max_num_index] = nl[max_num_index], nl[0]
                result.append(nl.pop(0))
                max_price(result, nl, change - 1)
    return result


# 리스트 중 가장 큰 값을 찾는다.
# -> 가장 큰 값의 index가 0이면 -> result에 그 값을 넣고 nl에서 pop(0) -> 다시 탐색 시작 but change는 그대로
# -> 가장 큰 값의 index가 0이 아니면 -> 0번째 값과 자리 변경 -> pop(0)를 통해 result에 값을 넣음 -> change -1
# -> 만약 nl의 크기가 2라면 서로 자리 변경 -> pop 없음 -> change - 1
# -> 최종적으로 change == 0이면 return result + nl

T = int(input())
for tc in range(1, T + 1):
    num, change = map(int, input().split())
    num_list = list(str(num))
    t_result = max_price([], num_list, change)
    result = ''
    for t in t_result:
        result += t
    print(f'#{tc} {result}')
