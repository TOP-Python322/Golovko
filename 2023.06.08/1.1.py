# ===== 1 =====


from string import ascii_letters, digits, punctuation


def strong_password(passwd : str = '123456') -> bool:
    """Check password strength for four criterions"""
    crit1 = len(passwd) > 7
    crit2 = len(set(ascii_letters) & set(passwd)) > 0
    crit3 = len([x for x in passwd if x in digits]) > 1
    crit4 = len(set(punctuation) & set(passwd)) > 0
    print(crit1 & crit2 & crit3 & crit4)


'''
>>> strong_password('aP3:kD_l3') 
True

>>> strong_password('password')   
False
'''
