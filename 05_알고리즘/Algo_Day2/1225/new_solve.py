# import sys
# sys.stdin = open('input.txt', 'r')
#
# for tc in range(1, 11):
#     input()
#     password = list(map(int, input().split()))
#     i = 0
#     num = 1
#     temp = []
#     while True:
#         i %= 8
#         if num == 6: num = 1
#         password[i] -= num
#         if password[i] <= 0:
#             password[i] = 0
#             temp = password[i+1:] + password[:i+1]
#             break
#         i += 1
#         num += 1
#     result = ''
#     for pw in temp:
#         result = result + str(pw) + ' '
#     print(f'#{tc} {result}')

import sys

sys.stdin = open('input.txt', 'r')

for _ in range(10):
    input()
    p = list(map(int, input().split()))
    i = -1
    n = 0
    while p[i]:
        i = (i + 1) % 8
        n = n % 5 + 1
        p[i] -= n
        if p[i] <= 0: p[i] = 0
    print(f'#{_+1} {" ".join(map(str, p[i+1:] + p[:i+1]))}')