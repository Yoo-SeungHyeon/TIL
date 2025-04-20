import sys
sys.stdin = open('input.txt', 'r')

# 노드 클래스로 선언해 객체로 다룸
class Node:
    def __init__(self, num, value, left = None, right = None): # left, right 기본값 지정
        self.num = int(num)
        self.value = value
        self.left = int(left) if left != None else None # None이면 그대로 아니면 정수로 변환
        self.right = int(right) if right != None else None # None이면 그대로 아니면 정수로 변환

# 숫자는 항상 leaf node임을 이용한 graph 계산 함수
def cal_graph(graph, index):
    # 노드 선언
    node = graph[index]

    # left 값이 None이면 지금 node 값 사용
    if node.left == None:
        return node.value
    else: # 숫자 또는 연산자 이면 추가로 계산
        num1 = int(cal_graph(graph, node.left))

    # right 값에 따라 left와 동일하게 연산
    if node.right == None:
        return node.value
    else:
        num2 = int(cal_graph(graph, node.right))

    # value에 맞는 반환값 세팅
    if node.value == '+':
        return num1 + num2
    elif node.value == '-':
        return  num1 - num2
    elif node.value == '*':
        return num1 * num2
    elif node.value == '/':
        return num1 / num2


for tc in range(1, 11):
    N = int(input())
    graph = [0]
    for _ in range(N):
        graph.append(Node(*input().split())) # Unpacking
    result = int(cal_graph(graph, 1))
    print(f'#{tc} {result}')
