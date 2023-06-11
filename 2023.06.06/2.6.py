# ===== 6 =====


letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
numbers = ('1', '2', '3', '4', '5', '6', '7', '8')
cell_1 = input("Укажите первую клетку\n")
cell_2 = input("Укажите вторую клетку\n")
letter_index_1 = letters.index(cell_1[0])
letter_index_2 = letters.index(cell_2[0])
number_index_1 = numbers.index(cell_1[1])
number_index_2 = numbers.index(cell_2[1])
if abs(letter_index_1 - letter_index_2) <= 1 and abs(number_index_1 - number_index_2) <= 1:
    print('да')
else:
    print('нет')


'''
Укажите первую клетку
d3
Укажите вторую клетку
e4
да

Укажите первую клетку
b2
Укажите вторую клетку
c4
нет
'''