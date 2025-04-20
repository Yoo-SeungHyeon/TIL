import sys
sys.stdin = open('input.txt', 'r')

# 자식노드를 더해서 본인의 값을 찾는 함수
def sum_chil(graph, index):
    # 본인 값이 존재하면 반환하면서 끝
    if graph[index] != None:
        return graph[index]

    # 자식 노드는 본인 인덱스의 2배와 2배+1 로 찾을 수 있음
    if graph[index*2] == None:
        chil1 = sum_chil(graph, index*2)
    else:
        chil1 = graph[index*2]

    # 완전 이진 트리는 좌측은 존재하나 우측은 존재하지 않을 수 있기 때문에 예외 처리
    try:
        if graph[index*2+1] == None:
            chil2 = sum_chil(graph, index*2+1)
        else:
            chil2 = graph[index*2+1]
    except:
        chil2 = 0 # 우측 노드 없으면 0을 반환해 값에 변화를 주지 않는다.

    # 자식 노드 2개의 값을 합하여 결과로 반환함
    return chil1 + chil2

T = int(input())
for tc in range(1, T+1):
    # N은 노드의 개수
    # M은 리프 노드의 개수
    # L은 출력할 노드 번호
    N, M, L = map(int, input().split())
    # N개의 리스트 생성
    graph = [None]*(N+1)
    for _ in range(M):
        index, value = map(int, input().split())
        graph[index] = value

    result = sum_chil(graph, L)
    print(f'#{tc} {result}')
