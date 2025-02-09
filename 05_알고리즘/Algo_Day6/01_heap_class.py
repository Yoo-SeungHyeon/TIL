class MinHeap:
    # 힙 자료구조 = 완전 이진 트리 = []
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)  # 마지막 노드에 값 추가
        # 힙 속성을 유지하기 위해 메서드를 호출
        self._sift_up(len(self.heap) - 1)  # len없이 그냥 -1로도 가능할듯?
        # self._sift_up(-1)  # 안된다!

    # 힙 속성 유지를 위한 보조 메서드
    def _sift_up(self, idx):
        # 부모 노드와 자신의 노드 값을 가져와 비교
        parent_idx = (idx - 1) // 2
        # 루트 노드에 도달할 때까지 계속 조사
        # 단, 본인의 값이 부모 노드 보다 클 때까지 진행
        while idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            # swap 이후 추가 조사할 인덱스 업데이트
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def heappop(self):
        # 기본적인 예외 처리
        if len(self.heap) == 0:
            raise IndexError('힙이 비었습니다.')
        # 길이가 1인 단순한 경우 처리
        if len(self.heap) == 1:
            return self.heap.pop()
        # 기본적인 루트 값 반환 및 마지막 노드 이동
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # 힙 상태 유지를 위한 shift_down 수행
        self._shift_down(0)
        return root

    # 삭제 후 최소 힙 상태를 유지하기 위한 보조 메서드
    def _shift_down(self, idx):
        # 가장 작은 요소의 인덱스를 초기화
        N = len(self.heap)
        smallest = idx
        left = idx * 2 + 1
        right = idx * 2 + 2

        # 왼쪽과 오른쪽 중 누구를 먼저 조사해야 하냐?
        # -> 힙은 완전 이진 트리
        # "왼쪽 자식 있음" & "오른쪽 자식 없음" -> 이런 경우는 존재
        # 하지만 "왼쪽 자식 없음" & "오른쪽 자식 있음" -> 이런 경우는 존재X

        if left < N and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < N and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._shift_down(smallest)  # 재귀적으로 자식 노드에 shift_down 진행

    # 리스트를 힙으로 바꿔주면 좋겠다~
    def heapify(self, array):
        self.heap = array[:]  # 주어진 리스트를 복사해서 heap에 할당
        N = len(self.heap)
        # heap 구조에 맞게 처리 -> leaf node 까지 반복 -> leaf node 여부는 len(heap) // 2 - 1로 알 수 있다.
        for idx in range(N // 2 - 1, -1, -1):
            self._shift_down(idx)


mh = MinHeap()
print(mh.heap)

mh.heappush(3)
mh.heappush(1)
mh.heappush(2)
print(mh.heap)
mh.heappush(0)
print(mh.heap)

print(mh.heappop())
print(mh.heap)

mh2 = MinHeap()
arr = [22, 12, 13, 15, 7, 1, 6]
mh2.heapify(arr)
print(mh2.heap)
