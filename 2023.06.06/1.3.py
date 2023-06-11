# ===== 3 =====


from  math import floor


minutes = int(input("Введите временной интервал в минутах\n"))
hours = floor(minutes / 60)
mins = minutes - hours * 60
print(f'{minutes} мин - это: {hours} час {mins} мин')


'''
Введите временной интервал в минутах
126
126 мин - это: 2 час 6 мин
'''