# ===== 5 =====


scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}


print('Введите слово')
word = input()
word = word.upper().replace('Ё', 'Е')
sum = 0
for i in word:
    for key, value in scores_letters.items():
        if i in value:
            sum += key
print(sum)

'''
Введите слово
синхрофазотрон
29
'''