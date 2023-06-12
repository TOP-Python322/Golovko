# ===== 4 =====


black_cells = ('a1', 'c1', 'e1', 'g1', 'a3', 'c3', 'e3', 'g3', 'a5', 'c5', 'e5', 'g5', 'a7', 'c7', 'e7', 'g7', 'b2', 'd2', 'f2', 'h2', 'b4', 'd4', 'f4', 'h4', 'b6', 'd6', 'f6', 'h6', 'b8', 'd8', 'f8', 'h8')
white_cells = ('a2', 'c2', 'e2', 'g2', 'a4', 'c4', 'e4', 'g4', 'a6', 'c6', 'e6', 'g6', 'a8', 'c8', 'e8', 'g8',
'b1', 'd1', 'f1', 'h1', 'b3', 'd3', 'f3', 'h3', 'b5', 'd5', 'f5', 'h5', 'b7', 'd7', 'f7', 'h7')
cell_1 = input("Укажите первую клетку\n")
cell_2 = input("Укажите вторую клетку\n")
if (cell_1 in black_cells and cell_2 in black_cells) or (cell_1 in white_cells and cell_2 in white_cells):
    print('да')
else:
    print('нет')


'''
Укажите первую клетку
a1
Укажите вторую клетку
b2
да

Укажите первую клетку
f6
Укажите вторую клетку
g4
нет
'''