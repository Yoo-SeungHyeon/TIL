import heapq

numbers = [9, 4, 12, 3, 7, 8, 11]

max_heap = []
for num in numbers:
    heapq.heappush(max_heap, -num)

print(max_heap)
largest = -heapq.heappop(max_heap)
print(largest)