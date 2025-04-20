import sys
sys.stdin = open('input.txt', 'r')

# 노드 정의
class Node:
    def __init__(self, num, value, left = None, right = None): # left, right 기본값 지정
        self.num = int(num)
        self.value = value
        self.left = int(left) if left != None else None # None이면 그대로 아니면 정수로 변환
        self.right = int(right) if right != None else None # None이면 그대로 아니면 정수로 변환

# in order 함수
def in_order(graph: list, index: int):
    left = graph[index].left
    right = graph[index].right
    value = graph[index].value

    # 왼쪽 먼저 탐색
    if left == None: # None 이면 값 출력하고 return
        print(value, end='')
        return
    else:
        in_order(graph, left) # 값이 존재하면 left 추가 탐색

    # 여기에 print(value)하면 right가 None일 때 value가 2번 출력됨 그래서 밑으로 보냄

    if right == None: # None 이면 값 출력하고 return
        print(value, end='')
        return
    else:
        print(value, end='') # value 출력하고 right 추가 탐색
        in_order(graph, right)

# 10번 입력받음
for tc in range(1, 11):
    N = int(input())
    # Node 객체를 입력받을 리스트 생성
    graph = [0] # 객체의 index를 편하게 계산하기 위해 0을 포함한 graph 생성.
    for _ in range(N):
        # Unpacking으로 인자 할당
        graph.append(Node(*input().split()))
    print(f'#{tc}', end=' ')
    in_order(graph, 1)
    print()
