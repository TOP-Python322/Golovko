# ===== 3 =====


import utils
from pathlib import Path


def ask_for_file() -> object:
    """Request from the user full path for file and return object of module"""
    while True:
        pth = input('путь: ')
        if Path(pth).exists():
            # module = utils.load_file(pth)
            return utils.load_file(pth)
        else:
            print('! по указанному пути отсутствует необходимый файл !')


'''
>>> config_module = ask_for_file()
путь: E:\Top-academy\2 семестр\HW\Golovko\2023.06.22\data\conf.py
>>> config_module.defaults
{'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
>>>
'''
