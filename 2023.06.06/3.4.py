# ===== 4 =====


n = int(input('Укажите количество разрядов\n'))
print()
min_num = int('1' * n)
max_num = int('9' * n)
count = 0
for item in range(min_num, max_num + 1):
    dividers = 0
    for i in range(1, item + 1):
        if item % i == 0:
            dividers += 1
        if dividers > 2:
            break  
    if dividers <= 2:
        count += 1
print(f'Количество простых чисел: {count}')


'''
Укажите количество разрядов
2

Количество простых чисел: 21
'''