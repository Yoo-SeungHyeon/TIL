from collections import deque


def BFS(node):
    queue = deque([node])
    result = []
    while queue:
        now = queue.popleft()
        result.append(tree[now][0])
        for child in tree[now][1:]:
            queue.append(child)
    return result

# 트리의 정보 입력 {어제(딕셔너리 사용했음)와 다르게 리스트로 입력}
# 우리끼리 트리를 리스트로 어떻게 표현할지 규칙을 정해보자.
# 1. 0번 인덱스 사용할건가? -> No! -> 기본값으로 빈 리스트가 아닌 [0] 또눈 [None]을 제공하자
# 2. 각 노드가 가지고 있을 값이 중요한가? -> Yes! -> 이차원 리스트로 값도 표현하자
# 3. 자식 노드는 어떻게 표현할거냐? -> 값 처럼 이차원 리스트로 표현하자!
tree = [
    None,
    ['A', 2, 3, 4],
    ['B', 5, 6],
    ['C'],
    ['D', 7, 8, 9],
    ['E'], ['F'], ['G'], ['H'], ['I']
]


result = BFS(1)
print(result)