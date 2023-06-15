from pathlib import Path
from re import compile, S
from sys import path


cwd = Path(path[0])

file_pat = compile(r'\d\.\d\.py')
mcom_pat = compile(r"'''.*?'''", S)

for file in cwd.iterdir():
    if file_pat.fullmatch(file.name):
        print(file.name)
        text = file.read_text(encoding='utf-8')
        for mo in mcom_pat.finditer(text):
            print(mo)
