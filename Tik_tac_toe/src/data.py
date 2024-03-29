"""
Вспомогательный модуль: глобальные переменные и условные константы.
"""

# стандартная библиотека
from pathlib import Path
from re import compile
from sys import path




APP_TITLE = 'КРЕСТИКИ-НОЛИКИ'

ROOT_DIR = Path(path[0]).parent
PLAYERS_DB_PATH = ROOT_DIR / 'data/players.ini'
SAVES_DB_PATH = ROOT_DIR / 'data/saves'

name_pattern = compile(r'[a-zA-Zа-яА-Я][а-яА-Я\w]+')

# база игроков - имена и статистика игроков 
players_db: dict[str, dict[str, int]] = {}


COMMANDS = {
    'помощь': ('help', 'помощь'),
    'новая партия': ('new', 'игра'),
    'загрузка': ('load', 'загрузка'),
    'авторизация': ('player', 'игрок'),
    'статистика': ('table', 'таблица'),
    'размер поля': ('dim', 'размер'),
    'выход': ('quit', 'выход'),
}
MESSAGES = {
    'ввод команды': '\n _ введите команду: ',
    'ввод имени': '\n _ введите имя: ',
    'режим игры': ('\nодин человек - 1, два человека - 2: '),
    'имя игрока': ('\nИмя игрока: '),
    'имя второго игрока': ('\nИмя второго игрока: '),
    'сложность игры с ботом': ('\nлёгкая - Л/л, сложная - С/с: '),
    'некорректное имя': ' ! имя игрока должно начинаться с буквы и быть не короче двух символов',
    # '': '',
}


# authorized_player: str = None
active_players: list[str] = []

TOKENS = ('X', 'O')

dim: int = 3
# dim_range: range = range(dim)
all_cells: int = dim**2

field_template: str = None

board: dict[int, str] = dict.fromkeys(range(all_cells), ' ')
# turns: dict[int, str] = {}
turns: list[int] = []
bot_game = True
hardness = False
