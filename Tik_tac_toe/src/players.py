"""
Основной модуль: взаимодействие с игроками.
"""

# проект
import data
import utils
import  re


# def get_name() -> None:
def get_name(name: str) -> None: 
    """Get the player's name and put it into the players database"""
    while True:
        if not data.name_pattern.fullmatch(name):
            print(data.MESSAGES['некорректное имя'])
            continue
        else:
            break
    if name not in data.players_db:
        data.players_db[name] = {
            'wins': 0,
            'fails': 0,
            'ties': 0
        }
    # if data.authorized_player is None:
    #     data.authorized_player = name
    data.active_players += [name]
    utils.write_players()
    return True
