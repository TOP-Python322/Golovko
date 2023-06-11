# ===== 4 =====


print('Введите данные')
data = {}
while True:
    t = input()
    if t == '':
        break
    s = t.split(' ')
    data.update({s[0]:s[1]})

val = input('Введите значение\n')
crit = False
for key, value in data.items():
    if value == val:
        print(key)
        crit = True
        break
        
if not crit:
    print('! value error !')


'''
Введите данные
1004 ER_CANT_CREATE_FILE
1005 ER_CANT_CREATE_TABLE
1006 ER_CANT_CREATE_DB   
1007 ER_DB_CREATE_EXISTS 
1008 ER_DB_DROP_EXISTS
1010 ER_DB_DROP_RMDIR 
1016 ER_CANT_OPEN_FILE
1022 ER_DUP_KEY       

Введите значение
ER_CANT_CREATE_FILE
1004


Введите данные
1004 ER_CANT_CREATE_FILE
1005 ER_CANT_CREATE_TABLE
1006 ER_CANT_CREATE_DB   
1007 ER_DB_CREATE_EXISTS 
1008 ER_DB_DROP_EXISTS   
1010 ER_DB_DROP_RMDIR    
1016 ER_CANT_OPEN_FILE
1022 ER_DUP_KEY       

Введите значение
ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
! value error !
'''