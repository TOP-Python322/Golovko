suits = ('черви', 'бубны', 'пики', 'трефы')

def deck():
    """Create ranked list of playing cards."""
    for suit in suits:
        for rank in range(2, 15):
            yield (rank, suit)


'''
 11:48:51 > python -i 2.py
>>> list(deck())[::13]
[(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
>>> list(deck())[8:13]
[(10, 'черви'), (11, 'черви'), (12, 'черви'), (13, 'черви'), (14, 'черви')]
'''
