from string import ascii_letters, digits, punctuation


# ИСПРАВИТЬ: согласно условию, аргумент должен быть обязательным — то есть без значения по умолчанию
def strong_password(passwd: str = '123456') -> bool:
    """Check password strength for four criteria."""
    crit1 = len(passwd) > 7
    # ИСПРАВИТЬ: эта проверка не гарантирует наличие буквенных символов обоих регистров (см. пример ниже)
    crit2 = len(set(ascii_letters) & set(passwd)) > 0
    crit3 = len([x for x in passwd if x in digits]) > 1
    # ИСПРАВИТЬ: согласно условию, в пароле должны присутствовать символы прочих категорий, а не только знаки препинания (см. пример ниже)
    crit4 = len(set(punctuation) & set(passwd)) > 0
    # ИСПРАВИТЬ: здесь должен быть возврат, а не вывод в stdout
    print(crit1 & crit2 & crit3 & crit4)
    # КОММЕНТАРИЙ: в контексте логических выражений всё же рекомендуется использовать логические, а не побитовые операторы — последние предназначены в первую очередь для побитовых операций с числами (подробнее: https://realpython.com/python-bitwise-operators/#overview-of-pythons-bitwise-operators)


# >>> strong_password('aP3:kD_l3')
# True

# >>> strong_password('password')
# False

# >>> strong_password('aabbcc12!')
# КОММЕНТАРИЙ: а должно быть False
# True

# >>> strong_password('aaBBcc 12')
# КОММЕНТАРИЙ: а должно быть True
# False


# ИТОГ: нужно лучше — 3/7
