# stack 자료구조 구현 -> class 구현
class Stack:
    # stack은 자료를 얼마나 저장할 수 있을지 크기를 지정
    # 기본인자 사용해서, 사용자가 별도의 크기를 지정하지 않을 때에도, 최대 10간틔 stakc
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None]*capacity
        self.top = -1

    def push(self, item):
        self.top += 1
        self.items[self.top] = item

    def peek(self):
        return self.items[self.top]

    def pop(self):
        # item = self.items[self.top]
        item = self.peek()
        self.items[self.top] = None
        self.top -= 1
        return item


stack = Stack(5)
print('start : ', stack.items, stack.top)
stack.push(1)
stack.push(2)
stack.push(3)
print('setting : ', stack.items, stack.top)
print('peek : ', stack.peek(), stack.top)
print('after peek : ', stack.items)
print('pop : ', stack.pop(), stack.top)
print('after pop : ', stack.items)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print('over : ', stack.items)