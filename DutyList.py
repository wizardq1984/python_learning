import pandas as pd
import numpy as np
from datetime import datetime


def data_list(begin_Date, end_Date):
    date_l = [datetime.strftime(x, '%Y-%m-%d') for x in list(pd.date_range(start=begin_Date, end=end_Date))]
    return date_l

def duty_list(day_num, start_type):
    duty_l =
    return duty_l


type_1 = ['A', 'B', 'R', 'R', 'B', 'A', 'C']
type_2 = ['C', 'B', 'R', 'R', 'B', 'C', 'A']
type_3 = ['B', 'A', 'B', 'C', 'B', 'R', 'R']
type_4 = ['B', 'C', 'B', 'A', 'B', 'R', 'R']
type_5 = ['B', 'B', 'A', 'B', 'C', 'R', 'R']
type_6 = ['B', 'B', 'C', 'B', 'A', 'R', 'R']

Rule_list = []
Rule_list.extend(type_1)
Rule_list.extend(type_5)
Rule_list.extend(type_3)
Rule_list.extend(type_2)
Rule_list.extend(type_6)
Rule_list.extend(type_4)

User_List = ['Patrick', 'Black', 'Amber', 'Jingyu', 'Sam', 'Jason']

print(Rule_list)
print(len(Rule_list))