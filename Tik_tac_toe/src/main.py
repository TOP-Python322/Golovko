"""
Главный модуль: точка входа.
"""

# проект
import data
import game
import help
import players
import utils


print(utils.header_text(data.APP_TITLE, level=1))

# 1. Чтение файлов данных
# 2. ЕСЛИ первый запуск:
if not utils.read_players():
    # вывод раздела помощи 
    help.show_help()


# 3. Запрос имени игрока
# while True:
#     if players.get_name(input(data.MESSAGES['имя игрока'])):
#         break
#     else:
#         continue

players.get_name(input(data.MESSAGES['имя игрока']))
players.get_name(input(data.MESSAGES['имя игрока']))


# суперцикл (главное меню)
while True:
    # 4. Ожидание ввода команды игрока
    command = input(data.MESSAGES['ввод команды'])



    game.get_human_turn(command)



    if command in data.COMMANDS['новая партия']:
        pass
        # game.mode()
        # game.get_human_turn(command)
        # result = game.game()
        # if result:
        #     players.update()


    elif command in data.COMMANDS['размер поля']:
        utils.set_board_dimension()
    elif command in data.COMMANDS['выход']:
        break
    
    # utils.clear()

# 20. Действия перед завершением работы приложения
