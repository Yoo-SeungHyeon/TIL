# 단순 연결 리스트
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # data : 삽입할 데이터
    # position : 삽입할 위치
    def insert(self, data, position):
        # 새로운 노드 생성
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # 현재 위치는 SLL 시작지점
            current = self.head
            for _ in range(position-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
    