# ===== 1 =====


from datetime import date


name = input("Введите имя\n")
surname = input("Введите фамилию\n")
_date = int(input("Введите год рождения\n"))
age = date.today().year - _date
print(surname + ' ' + name + ', ' + str(age))


'''
Введите имя
Давид
Введите фамилию
Шапиро
Введите год рождения
1980
Шапиро Давид, 43
'''