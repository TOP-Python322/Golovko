# ===== 5 =====


integer_part = input("Введите целую часть числа миль\n")
fractional_part = input("Введите дробную часть числа миль\n")
miles = float(integer_part + '.' + fractional_part)
kilometers = miles * 1.61
print(f'{miles:.2f} миль = {kilometers:.2f} км')


'''
Введите целую часть числа миль
14
Введите дробную часть числа миль
23
14.23 миль = 22.91 км
'''