# ===== 2 =====


fruits =  []
print('Введите названия фруктов') 
while True:
    fruit = input()
    if fruit == '':
        break
    fruits.append(fruit)
s = ', '.join(fruits[:-1])
s += ' и ' + fruits[-1]
print(s)


'''
Введите названия фруктов
яблоко
груша
слива
виноград

яблоко, груша, слива и виноград
'''