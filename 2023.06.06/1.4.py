# ===== 4 =====


from  math import floor


numbr = int(input("Введите трёхзначное число\n"))
hundreds = int(numbr / 100)
dozens = int((numbr - hundreds * 100) / 10)
units = numbr - hundreds * 100 - dozens * 10
sum = hundreds + dozens + units
composition = hundreds * dozens * units
print(f'Сумма цифр: {sum}\nПроизведение цифр: {composition}')


'''
Введите трёхзначное число
345
Сумма цифр: 12
Произведение цифр: 60
'''