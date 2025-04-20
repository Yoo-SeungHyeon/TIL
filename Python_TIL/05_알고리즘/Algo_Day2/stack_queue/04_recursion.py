# 재귀 함수도 스택의 형태로 구현되고 동작한다.
def fact(item):
    if item == 1:
        return 1
    else:
        return item * fact(item-1)
fact(4)