# ===== 1 =====


mail = input('Введите адрес электронной почты\n')
if mail.find('@') == -1 or mail.find('.') == -1:   
    print('нет')
else:
    lenght = len(mail)
    index_at = mail.index('@')
    substr = mail[index_at + 1:]
    criteria1 = (index_at > 0) and (index_at < lenght - 1)
    criteria2 = (substr.index('.') > 0) and (substr.index('.') < len(substr) - 1)
    if criteria1 and criteria2:
        print('да')
    else:
        print('нет')


'''
Введите адрес электронной почты
qwer.we@dfgd.dfgrt.we
да

Введите адрес электронной почты
abcde@fghij
нет
'''