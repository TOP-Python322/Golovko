# ===== 2 =====


from math import floor


divisible = int(input("Введите делимое\n"))
divider = int(input("Введите делитель\n"))
if divisible % divider == 0:
    print(f'{divisible} делится на {divider} нацело')
    print(f'частное: {int(divisible / divider)}')
else:
    print(f'{divisible} не делится на {divider} нацело')
    print(f'неполное частное: {floor(divisible / divider)}')
    print(f'остаток: {divisible - floor(divisible / divider) * divider}')


'''
Введите делимое
12
Введите делитель
4
12 делится на 4 нацело
частное: 3

Введите делимое
10
Введите делитель
3
10 не делится на 3 нацело
неполное частное: 3      
остаток: 1
'''