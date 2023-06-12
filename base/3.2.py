# ===== 2 =====


n = int(input('Укажите количество целых чисел\n'))
print('Введите числа')
sum = 0
for i in range(n):
    num = int(input())
    if num > 0:
        sum += num
print(sum)


'''
Укажите количество целых чисел
6
Введите числа
3
-5
1
10
-1
8
22
'''