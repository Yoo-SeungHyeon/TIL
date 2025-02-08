# 모든 queue 문제를 class 부터 구현하는게 아니다. 라이브러리를 활용하자.
from collections import deque

queue = deque()
queue.append((1, 1))
queue.append((2, 2))
queue.append((3, 3))
queue.append((4, 4))
print(queue)
print(queue.popleft())
print(queue)
print(queue.pop())
print(queue)