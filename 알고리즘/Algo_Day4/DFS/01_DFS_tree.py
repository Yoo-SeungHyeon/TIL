# 트리의 구조를 선언
tree = {'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'D': ['G', 'H', 'I']}

def dfs(node):
    # 노드 탐색
    print(node)
    # 자식 노드 존재 확인
    # if not tree.get(node): return
    # 자식 노드 탐색
    # for child in tree[node]: dfs(tree, child)

    for child in tree.get(node, []): #  파이썬의 for문은 비어있는 리스트에 대해서는 코드 수행을 하지 않음
        dfs(child)

dfs('A')