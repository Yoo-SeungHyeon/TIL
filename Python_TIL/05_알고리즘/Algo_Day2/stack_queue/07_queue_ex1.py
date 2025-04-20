queue = []
candy = 20
queue.append((1, 1)) # 1번이 처음으로 1개 가져간다.
result = None

while candy > 0:
    print(queue, candy)
    person, acc = queue.pop(0)
    if candy - acc <= 0:
        result = person
        break
    candy -= acc
    queue.append((person, acc + 1))
    queue.append((len(queue)+1, 1))
print(result)