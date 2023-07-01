from shutil import copy2, get_terminal_size


def important_message(text : str) -> str:
    """Generate string with given message rounded by the frame which consists from symbols '#' and '='."""
    width = get_terminal_size()[0] - 1
    text_width = width - 2 - 4
    txt = text.split()

    ss = '#' + '=' * (width - 2) + '#\n'
    ss += '#' + ' ' * (width - 2) + '#\n'
    indx = 0
    prev_indx = 0
    temp_string = ''
    for i in txt:
        temp_string += txt[indx] + ' '
        if len(temp_string) > text_width:
            temp_list = txt[prev_indx : indx]
            temp_string = ' '.join(temp_list) 
            temp_string = temp_string.center(text_width, ' ')
            temp_string = '#  ' + temp_string + '  #\n'
            ss += temp_string
            temp_string = ''
            prev_indx = indx
        else:
            indx += 1

    temp_list = txt[prev_indx : ]
    temp_string = ' '.join(temp_list) 
    temp_string = temp_string.center(text_width, ' ')
    temp_string = '#  ' + temp_string + '  #\n'
    ss += temp_string
    ss += '#' + ' ' * (width - 2) + '#\n'
    ss += '#' + '=' * (width - 2) + '#\n'
    return ss


def load_file(file_path : str) -> object:
    """Make copy of given file and load it as module""" 
    copy2(file_path, './file_copy.py')
    import file_copy as module
    return module


def add_context(in_list, num, indx):
    """Add context to line"""
    inf = max(indx - num, 0)
    sup = min(indx + num, len(in_list) - 1) + 1
    result = in_list[inf : sup]
    return ''.join(result).replace('\n',' ')
