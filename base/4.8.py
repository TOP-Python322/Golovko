# ===== 8 =====


inp = input('Введите список фалов\n')
print()
inp_list = inp.split('; ')
inp_list = sorted(inp_list)
out_list = []
cur_index = 0
while cur_index < len(inp_list):
    finding = inp_list[cur_index]
    out_list.append(finding)
    if cur_index == len(inp_list) - 1:
        break
    repeat = 1
    if len(inp_list) > 1:
        while True:
            if finding == inp_list[cur_index + 1]:
                repeat += 1
                cur_index += 1
                dot_position = finding.index('.')
                name = finding[:dot_position] + '_' + str(repeat)
                extension = finding[dot_position:]
                out_list.append(name + extension)
            else:
                break
    cur_index += 1

s = ''
for i in out_list:
    s += f'{i}\n'
print(s[:-1])


'''
Введите список фалов
1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz; write.html

1.py
1_2.py
1_3.py
aux.h
functions.h
main.cpp
main_2.cpp
main_3.cpp
src.tar.gz
src_2.tar.gz
write.html
'''