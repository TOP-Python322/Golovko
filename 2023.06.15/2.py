# ===== 2 =====


suits  = ('черви', 'бубны', 'пики', 'трефы')     
royalty = {11 : 'валет', 12 : 'дама', 13 : 'король', 14 : 'туз'}


def deck():
    """Create ranked list of playing cards"""
    for i in suits:
        for k in range(2, 11):
            result = (k, i)
            yield result
        for k in range(11, 15):
            result = (royalty[k], i)
            yield result


'''
>>> list(deck())[::13]
[(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
'''
