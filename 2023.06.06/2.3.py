# ===== 3 =====


year_num = int(input("Введите год\n"))
if (year_num % 4 == 0 and year_num % 100 != 0) or year_num % 400 == 0:
    print('да')
else:
    print('нет')


'''
Введите год
2020
да

Введите год
1987
нет
'''