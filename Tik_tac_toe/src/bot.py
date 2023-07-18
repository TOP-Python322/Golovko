"""
Основной модуль: вычисления для бота.
"""

import random
import data
import game

def bot_move():
    """Make the bot move"""
    global turns
    global who

    if data.hardness:
        # here the code of complex bot
        return
    else:
        move = [x for x in range(data.all_cells) if x not in data.turns]
        if move:
            move = random.choice(move)
        else:
            pass
            # game.game_over()
    data.turns.append(move)
    game.print_board()
    game.check_win()
    game.who = (game.who + 1) % 2
    return
