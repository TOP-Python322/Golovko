import configparser
import re
from string import ascii_letters
from shutil import get_terminal_size


russian_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
players = []
board_variant = 0
turns = []
dimension = 0
hardness = False
bot_game = True
who = 0
left_space = ''
cell_width = 0


def read_config(file_name: str):
    """Read from config file the data of saved games"""
    config = configparser.ConfigParser()
    # with open(file_name, 'r', encoding = 'utf-8') as configfile:
    #     pass
    config.read(file_name)


def write_config(file_name: str):
    """Save the game into config file"""
    # global turns

    config = configparser.ConfigParser()
    config.read(file_name)
    turns_ = ', '.join([str(x) for x in turns])
    players_pair = frozenset((players[0], players[1]))
    config['Games'].update({repr(players_pair): repr({'X': players[0],\
                            'turns': turns_, 'dim': dimension})})
    config['Statistics'] = {'Empty': ''}
    with open(file_name, 'w', encoding = 'utf-8') as configfile:
        config.write(configfile)



def important_message(msg : str) -> str:
    """Show centered message in the frame"""

    width = get_terminal_size()[0] - 1
    padding = 20
    frame_width = width - padding
    line_width = frame_width - 2 - 4
    buffer = msg.split(' ')
    last_word = len(buffer)
    out_string = ''
    test_string = ''
    prev_indx = 0 
    indx = 0
    out_string = ('#' + '=' * (frame_width - 2) + '#').center(width,' ') + '\n'
    out_string += ('#' + ' ' * (frame_width - 2) + '#').center(width,' ') + '\n'
    while True:
        test_string += buffer[indx] + ' '
        if len(test_string) <= line_width:
            indx += 1
            if indx == last_word:
                out_string += ('#  ' + test_string[:-1].center(line_width, ' ') + '  #').center(width,' ') + '\n'
                break
        else:
            out_string += ('#  ' + ' '.join(buffer[prev_indx: indx]).center(line_width, ' ') + '  #').center(width,' ') + '\n'
            prev_indx = indx
            test_string = ''
    out_string += ('#' + ' ' * (frame_width - 2) + '#').center(width,' ') + '\n'
    out_string += ('#' + '=' * (frame_width - 2) + '#').center(width,' ') + '\n'
    print(out_string)


def help():
    """Show game rules"""
    msg = 'Крестики-нолики — логическая игра между двумя противниками'\
    ' на квадратном поле 3 на 3 клетки или большего размера.'\
    '                                                        '\
    '                                         '\
    'Правила игры: '\
    'Игроки по очереди ставят на свободные клетки поля N×N знаки (один' \
    ' всегда крестики, другой всегда нолики). Первый, выстроивший в ряд '\
    'N своих фигуры по вертикали, горизонтали или большой диагонали,'\
    ' выигрывает. Если игроки заполнили все N×N ячеек и оказалось, '\
    'что ни в одной вертикали, горизонтали или большой диагонали' \
    'нет трёх одинаковых знаков, партия считается закончившейся' \
    'в ничью. Первый ход делает игрок, ставящий крестики. '\
    'Для ввода своих ходов игроки могут использовать четыре варианта:'\
    ' указать номер клетки (клетки считаютя слева направо'\
    ' и сверху вниз, нумерация начинается с нуля (вариант № 1)'\
    ' или с единицы (вариант № 2)) или по координатному принципу -'\
    ' ввести номер строки, потом через пробел номер столбца,'\
    ' нумерация строк и столбцов начинается с нуля (вариант № 3)'\
    ' или с единицы (вариант № 4). При игре с ботом можно выбрать'\
    ' один из двух уровней сложности. Для ввода имен игроков можно '\
    ' использовать буквы только английского или русского алфавита.'
    important_message(msg)


def menu():
    print('\nГЛАВНОЕ МЕНЮ:\n')
    print('LOAD[L/l] - ЗАГРУЗИТЬ СОХРАНЕННУЮ ИГРУ')
    print('NEW[N/n] - НОВАЯ ИГРА')
    print('HELP[H/h] - ПОМОЩЬ')    
    print('QUIT[Q/q] - ВЫХОД')


def game_over():
    if not players or not turns:
        return
    write_config('saved_games.ini')



def show_board():
    """Show game board"""

    if who:
        space = left_space
    else:
        space = ''

    board_view = ''
    for y in range(dimension):
        line = ''
        for x in range(dimension):
            cell_number = x + y * dimension
            symbol = ' '
            if cell_number in turns:
                if turns.index(cell_number) % 2:
                    symbol = 'O'
                else:
                    symbol = 'X'
            line += f' {symbol} |'
        line = f'{space}{line[:-1]}\n'
        border = ('—' * cell_width * dimension)[:-1]
        board_view += f'{line}{space}{border}\n'
    print(f'{board_view[:- dimension * cell_width - len(space)]}\n')


def show_variants():
    """Show possible variants of input"""
    var1 = '№ 1\n 0 | 1 | 2 \n———————————\n 3 | 4 | 5 \n'\
           '———————————\n 6 | 7 | 8 \n'
    var2 = '№ 2\n 1 | 2 | 3 \n———————————\n 4 | 5 | 6 \n'\
           '———————————\n 7 | 8 | 9 \n'
    var3 = '№ 3\n 0 0 | 0 1 | 0 2 \n—————————————————\n '\
           '1 0 | 1 1 | 1 2 \n—————————————————\n 2 0 | 2 1 | 2 2 \n'
    var4 = '№ 4\n 1 1 | 1 2 | 1 3 \n—————————————————\n '\
           '2 1 | 2 2 | 2 3 \n—————————————————\n 3 1 | 3 2 | 3 3 \n'

    space = ' ' * 7
    var1 = var1.split('\n')
    var2 = var2.split('\n')
    var3 = var3.split('\n')
    var4 = var4.split('\n')
    one_table_width = len(var3[1])
    lines_count = len(var1)

    variants_string = '\n'
    for i in range(lines_count):
        variants_string += var1[i].center(one_table_width,' ') + space +\
        var2[i].center(one_table_width,' ') + space + \
        var3[i].center(one_table_width,' ') +\
        space + var4[i].center(one_table_width,' ') + '\n'
    print(variants_string)


def check_move(inp: str):
    """Check player movement correctness and record it to list"""
    global board_variant
    global turns
    global who

    wrong_turn = False

    if board_variant in (1, 2):
        if set(inp) - set('0123456789'):
            wrong_turn = True
        else:
            if board_variant == 1:
                indx = int(inp)
            elif board_variant == 2:
                indx = int(inp) - 1
            # if indx >= dimension ** 2:
            #     wrong_turn = True
            # else:
            #     turns.append(indx)
            #     show_board()
            #     who = (who + 1) % 2

    elif board_variant in (3, 4):
        if set(inp) - set('0123456789 ') or ' ' not in inp:
            wrong_turn = True
        else:
            inp = inp.split(' ')
            if not inp:
                wrong_turn = True
            else:
                y = int(inp[0])
                x = int(inp[1])
                if board_variant == 4:
                    y -= 1
                    x -= 1
                indx = x + y * dimension

    # if indx >= dimension ** 2:
    #     wrong_turn = True

    if wrong_turn or indx >= dimension ** 2 or indx in turns:
        print('НЕПРАВИЛЬНЫЙ ХОД. ПОВТОРИТЕ!')
        return
    
    turns.append(indx)
    show_board()
    who = (who + 1) % 2


def load_game(file_name: str) -> None:
    """"Load saved game"""
    while True:
        inp = input('ИМЯ ИГРОКА: ')
        if not set(inp) - set(ascii_letters) or not set(inp) - set(russian_letters):
            config = configparser.ConfigParser()
            config.read(file_name)
            games = config['Games']
            for key, value in games.items():
                if inp in key:
                    print(value)
                    # (?<=abc)def
                    m = re.search('(?<=\'turns\'\:)[^\']*', value)
                    print(m.group(0))
            return
        else:
            continue


def new_game():
    global bot_game
    global dimension
    global hardness
    global players
    global board_variant
    global turns
    global left_space
    global cell_width

    while True:
        # Выбор размера игрового поля
        while True:
            inp = input('УКАЖИТЕ РАЗМЕР ИГРОВОГО ПОЛЯ [3-20]: ')
            dimension = int(inp)
            if 3 <= dimension <= 20:
                break
            else:
                continue

        # Выбор варианта нумерации клеток
        show_variants()
        while True:   
            board_variant = int(input('ВЫБЕРИТЕ ВАРИАНТ НУМЕРАЦИИ КЛЕТОК [1-4]: '))
            if 1 <= board_variant <= 4:
                terminal_width = get_terminal_size()[0] - 1
                if board_variant in (1, 2):
                    cell_width = 4
                elif board_variant in (3, 4):
                    cell_width = 6
                left_space = ' ' * (terminal_width - cell_width * dimension)
                break
            else:
                continue

        # Выбор режима игры
        inp = input('ВЫБЕРИТЕ РЕЖИМ ИГРЫ [1-ОДИН ЧЕЛОВЕК, 2-ДВА ЧЕЛОВЕКА]: ')
        if inp == '1':
            bot_game = True
            while True:
                inp = input('ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ БОТА [1-ЛЁГКИЙ, 2-СЛОЖНЫЙ]: ')
                if inp == '1':
                    hardness = False
                    break
                elif inp == '2':
                    hardness = True
                    break
                else:
                    continue
            inp = input('ВВЕДИТЕ ИМЯ ИГРОКА: ')
            players.append(inp)
            players.append('COMPUTER')
            break
        elif inp == '2':
            print('Human')
            bot_game = False
            inp = input('ВВЕДИТЕ ИМЯ ПЕРВОГО ИГРОКА: ')
            players.append(inp)
            inp = input('ВВЕДИТЕ ИМЯ ВТОРОГО ИГРОКА: ')
            players.append(inp)
            break
        else:
            continue


def main():
    global bot_game
    global dimension
    global hardness
    global players


    # Чтение файлов данных
    read_config('saved_games.ini')


    help()
    menu()

    # Main loop
    while True:
        inp = input('==>: ').upper()
        if inp:
            if inp in ('QUIT', 'Q'):
                game_over()
                return
            elif inp in ('HELP', 'H'):
                help()
            elif inp in ('LOAD', 'L'):
                load_game('saved_games.ini')
            elif inp in ('NEW', 'N'):
                new_game()
                print(players)
            else:
                check_move(inp)


main()
