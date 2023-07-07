from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase


def strong_password(passwd: str) -> bool:
    """Check password strength for four criteria."""
    crit1 = len(passwd) > 7
    crit2 = (len(set(ascii_lowercase) & set(passwd)) > 0) \
        and len(set(ascii_uppercase) & set(passwd)) > 0
    crit3 = len([x for x in passwd if x in digits]) > 1
    crit4 = len(set(passwd) - set(ascii_letters) - set(digits)) > 0
    return (crit1 and crit2 and crit3 and crit4)


'''
  8:50:33 > python -i 1.py
>>> strong_password('aP3:kD_l3')
True
>>> strong_password('password')
False
>>> strong_password('aabbcc12!')
False
>>> strong_password('aaBBcc 12')
True
'''
