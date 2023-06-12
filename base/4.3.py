# ===== 3 =====


print('Введите через пробел элементы первого списка')
s1 = input()
print('Введите через пробел элементы второго списка')
s2 = input()
s1 = s1.replace(' ','')
s2 = s2.replace(' ','')
l1 = list(s1)
l2 = list(s2)
crit = False
for i in range(len(l1)):
    if l1[i] == l2[0]:
        crit = True
        for k in range(len(l2)):
            if l2[k] != l1[k+i]:
                crit = False
                break
        if crit:
            break
if crit:
    print('да')
else:
    print('нет')


'''
This task can be resolved without conversion to 'int'
s1 = s1.replace(' ','')
s2 = s2.replace(' ','')
if s1.find(s2) != -1:
    print('да')
else:
    print('нет')
'''


'''
Введите через пробел элементы первого списка
1 2 3 4 5
Введите через пробел элементы второго списка
2 3 4
да

Введите через пробел элементы первого списка
1 2 3 4 5
Введите через пробел элементы второго списка
2 6 7
нет
'''