# 아래에 코드를 작성하시오.
seat = [['O','O','O'],['O','O','O'],['O','O','O']]
seat[0][2] = 'X'
seat[1][0] = 'X'
seat[1][2] = 'X'
seat[2][0] = 'X'
seat[2][2] = 'X'
print("현재 좌석 배치:")
for i in seat:
    print(f'{i[0]} {i[1]} {i[2]}')