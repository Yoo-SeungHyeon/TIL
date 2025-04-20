import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    string = input()
    bar = 0
    result = 0
    lazer = False
    for char in string:
        if char == '(':
            lazer = True
            bar += 1
        elif char == ')' and lazer:
            bar -= 1
            result += bar
            lazer = False
        elif char == ')' and not lazer:
            bar -= 1
            result += 1
    print(f'#{tc} {result}')