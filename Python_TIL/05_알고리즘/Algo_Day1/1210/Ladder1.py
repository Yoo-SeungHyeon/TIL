import sys
sys.stdin = open("input.txt", "r")

'''
1. position의 좌,우,하를 살핀다.
2. 좌 or 우 에 1이 존재하면 그쪽으로 이동
3. 해당 방향으로 진행할 때는 down방향이 존재하면 그쪽으로 이동
'''

for _ in range(10):
    # test case 입력
    tc = input()
    
    # 배열 입력
    data = []
    for _ in range(100):
        data.append(list(map(int, input().split())))

    # 각각의 스타팅 포인트에서 시작
    for i in range(100):
        start = data[0][i]
        depth = 0
        # 값이 1이면 시작
        if start == 1:
            j = i
            while depth != 99:
                left = data[depth][j-1] if j-1 >= 0 else 0
                right = data[depth][j+1] if j+1 <= 99 else 0
                if left == 1:
                    j -= 1
                    down = data[depth+1][j]
                    while not down:
                        j -= 1
                        down = data[depth+1][j]
                    depth += 1
                elif right == 1:
                    j += 1
                    down = data[depth+1][j]
                    while not down:
                        j += 1
                        down = data[depth + 1][j]
                    depth += 1
                else:
                    depth += 1
            if data[depth][j] == 2:
                print(f"#{tc} {i}")