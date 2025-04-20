# 아래에 코드를 작성하시오.
numbers = list(range(1, 11))
for num in numbers:
    if num == 5:
        break
    if num % 2 == 0:
        print(num)
    elif num % 2 == 1:
        print(f'{num}은(는) 홀수')