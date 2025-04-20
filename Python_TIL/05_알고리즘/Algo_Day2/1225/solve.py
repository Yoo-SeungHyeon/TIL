import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

for _ in range(10):
    tc = int(input())
    queue = deque(map(int, input().split()))
    num = 1
    while True:
        head = queue.popleft()
        head -= num
        if num == 5:
            num = 0
        num += 1
        if head <= 0:
            head = 0
            queue.append(head)
            break
        else:
            queue.append(head)
    result = ' '.join(map(str,queue))
    print(f'#{tc} {result}')