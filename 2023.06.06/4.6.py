# ===== 6 =====


signs = {'0', '1'}
n = input('Введите двоичное число\n')
if n.startswith('b'):
    n = n[1:]
elif n.startswith('0b'):
    n = n[2:]
ns = set(n)
if not ns.issubset(signs):
    print('нет')
else:
    print('да')


'''
Введите двоичное число
0b10110110
да

Введите двоичное число
1b0101
нет
'''