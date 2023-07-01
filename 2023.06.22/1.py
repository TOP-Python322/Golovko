# ===== 1 =====


from pathlib import Path


def list_files(path : str) -> tuple | None:
    """Non-recursive search of files in the given directory"""
    p = Path(path)
    if p.exists():
        _ = [x.name for x in p.iterdir() if x.is_file()]
        return tuple(_)
    else:
        return None


'''
>>> list_files('./data')
('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
'''
