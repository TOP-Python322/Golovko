# ===== 5 =====


from math import floor


sym = ',.;:?!"`*/() '
t = input('Введите текст телеграммы\n')
print()
for i in sym:
    t = t.replace(i, '')
length = len(t)
kopecks = length * 30
rubles = floor(kopecks / 100)
kopecks = kopecks - rubles * 100
print(f'{rubles} руб. {kopecks} коп.')


'''
Введите текст телеграммы
Графиня бежит пруду изменившимся лицом

10 руб. 20 коп.
'''