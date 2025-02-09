examples = 'if (( i == 0 ) $$ ( j == 0 )'

def check(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # stack이 비었거나 동일한 소괄호가 아니라면
            if not stack or stack[-1] != '(' :
                return False
            # 조건을 만족하면 pop 한다.
            stack.pop()
    return not stack

