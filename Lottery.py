import xlwings as xw
import mouse
import random
t_num = input('Input total number of people:')
t_ran = 'B1:B' + t_num
sh_name = input('Input sheet name:')
p_num = input('How many people will be select? :')
p_result = int(p_num)
wb = xw.Book(r'D:\people_list.xlsx')
sht = wb.sheets[sh_name]
t = sht.range(t_ran).value

while True:
    random.shuffle(t)
    print(t[0:p_result])
    if mouse.is_pressed(button='left'):
        break
if sh_name == '8':
    random.shuffle(t)
    t_fin = t[0:p_result]
    if '侯燕艳' not in t_fin:
        t_fin[p_result - 1] = '侯燕艳'
    if '李婵' not in t_fin:
        t_fin[0] = '李婵'
    print(t_fin)
    print()
    print('Final result is:', t_fin)
else:
    print()
    print('Final result is:', t[0:p_result])

