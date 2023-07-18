"""
Основной модуль: настройка игры и игровой процесс.
"""


import data
import utils
import bot
import players


who = 0

def game() -> list[str] | None:
    """Контроллер игрового процесса.
    
    Возвращает список имён в формате ['имя_выигравшего', 'имя_проигравшего'], пустой список для ничьей или None, если партия не завершена.
    """
    data.field = utils.field_template()
    # 10. Цикл до максимального количества ходов
    for t in range(len(data.turns), data.all_cells):
        # индекс-указатель на игрока и токен
        parity = t % 2
        
        # шаги 11–13
        ...
    else:
        utils.header_text('ничья', level=2)
        return []


def get_human_turn(inp: str):
    """Check player movement correctness and record it to list"""

    global turns
    global who

    wrong_turn = False
    if set(inp) - set('0123456789'):
        wrong_turn = True
    else:
        indx = int(inp)
    
    if wrong_turn or indx >= data.dim ** 2 or indx in data.turns:
        print('НЕПРАВИЛЬНЫЙ ХОД. ПОВТОРИТЕ!')
        return

    data.turns.append(indx)
    print_board()
    check_win()
    who = (who + 1) % 2
    if data.bot_game:
        bot.bot_move()
    else:
        return


def save():
    ...


def print_board():
    """Show game board"""

    board_view = f'{data.active_players[1]:>{utils.term_width}}:\n' \
                    if who else f'{data.active_players[0]}:\n'
    for y in range(data.dim):
        line = ''
        for x in range(data.dim):
            cell_number = x + y * data.dim
            symbol = ' '
            if cell_number in data.turns:
                if data.turns.index(cell_number) % 2:
                    symbol = data.TOKENS[1]
                else:
                    symbol = data.TOKENS[0]
            line += f' {symbol} |'
        if who:
            line = f'{line[:-1]:>{utils.term_width}}\n'
            border = ('—' * 4 * data.dim)[:-1]
            board_view += f'{line}{border:>{utils.term_width}}\n'
        else:
            line = f'{line[:-1]}\n'
            border = ('—' * 4 * data.dim)[:-1]
            board_view += f'{line}{border}\n'
    print(f'{board_view[:- data.dim * 4]}\n')
    return


def check_win():
    """..."""




def game_over():
    if not data.active_players or not turns:
        return

def mode():
    """Select mode of the game: bot or human"""

    while True:
        command = input(data.MESSAGES['режим игры'])
        if command == '1':
            data.bot_game = True
            while True:
                command = input(data.MESSAGES['сложность игры с ботом'])
                if command in ('Л', 'л'):
                    data.hardness = False
                    players.get_name('LiteBot')
                    break
                elif command in ('С', 'с'):
                    data.hardness = True
                    players.get_name('HardBot')
                    break
                else:
                    continue
            break
        elif command == '2': 
            data.bot_game = False
            while True:
                if players.get_name(input('Имя второго игрока')):
                    break
                else:
                    continue
            break
        else:
            continue
    return
