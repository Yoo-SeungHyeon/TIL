import sys
sys.stdin = open('sample_input.txt', 'r')
#
# def move_func(ele):
#     if ele[2] == 0:
#         ele[1] += 1
#     elif ele[2] == 1:
#         ele[1] -= 1
#     elif ele[2] == 2:
#         ele[0] -= 1
#     elif ele[2] == 3:
#         ele[0] += 1
#     return ele

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    elements = []
    for _ in range(N):
        elements.append(list(map(int, input().split())))

    result = 0
    # 약 2000초 동안 진행
    for _ in range(1000):
        # 남은 원자가 없으면 종료
        if not elements:
            break

        # 1씩 이동
        for i in range(len(elements)):
            if elements[i][2] == 0:
                elements[i][1] += 1
            elif elements[i][2] == 1:
                elements[i][1] -= 1
            elif elements[i][2] == 2:
                elements[i][0] -= 1
            elif elements[i][2] == 3:
                elements[i][0] += 1

        # 충돌 확인
        crash = []
        for i in range(len(elements)):
            temp = []
            for j in range(i+1, len(elements)):
                node1 = elements[i]
                node2 = elements[j]
                if node1[0] == node2[0] and node1[1] == node2[1]:
                    temp.append(j)
            if temp:
                temp.append(i)
                crash.extend(temp)

        # 충돌이 발생한 노드 제거
        not_dupl_crash = list(set(crash))
        new_list = []
        for e in range(N):
            if not e in not_dupl_crash:
                new_list.append(elements[e])
            else:
                result += elements[e][3]

        elements = new_list

    print(f'#{tc} {result}')