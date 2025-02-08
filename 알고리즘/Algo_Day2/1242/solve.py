import sys
sys.stdin = open('sample_input.txt', 'r')
def hex_bin(str):
    result = ''
    for char in str:
        if char == '0':
            result += '0000'
        elif char == '1':
            result += '0001'
        elif char == '2':
            result += '0010'
        elif char == '3':
            result += '0011'
        elif char == '4':
            result += '0100'
        elif char == '5':
            result += '0101'
        elif char == '6':
            result += '0110'
        elif char == '7':
            result += '0111'
        elif char == '8':
            result += '1000'
        elif char == '9':
            result += '1001'
        elif char == 'A':
            result += '1010'
        elif char == 'B':
            result += '1011'
        elif char == 'C':
            result += '1100'
        elif char == 'D':
            result += '1101'
        elif char == 'E':
            result += '1110'
        elif char == 'F':
            result += '1111'
    return result

def get_num(str):
    if str == '0001101':
        return 0
    elif str == '0011001':
        return 1
    elif str == '0010011':
        return 2
    elif str == '0111101':
        return 3
    elif str == '0100011':
        return 4
    elif str == '0110001':
        return 5
    elif str == '0101111':
        return 6
    elif str == '0111011':
        return 7
    elif str == '0110111':
        return 8
    elif str == '0001011':
        return 9

# target1 = hex_bin('1DB176C588D26EC')[-58:-2]
# target2 = hex_bin('196EBC5A316C578')[-59:-3]
# target3 = hex_bin('328D1AF6E4C9BB')[-56:]
# sol_data1 = []
# sol_data2 = []
# sol_data3 = []
# for j in range(8):
#     sol_data1.append(get_num(target1[j * 7:j * 7 + 7]))
#     sol_data2.append(get_num(target2[j * 7:j * 7 + 7]))
#     sol_data3.append(get_num(target3[j * 7:j * 7 + 7]))
#
#
# print(sol_data1, sol_data2, sol_data3)

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
