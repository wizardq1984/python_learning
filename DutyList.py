import pandas as pd
import numpy as np
from datetime import datetime


def data_list(beginDate, endDate):
    date_l = [datetime.strftime(x, '%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l

if __name__ == '__main__':
type_1 = ['A','B','R','R','B','A','C']
type_2 = ['C','B','R','R','B','C','A']
type_3 = ['B','A','B','C','B','R','R']
type_4 = ['B','C','B','A','B','R','R']
type_5 = ['B','B','A','B','C','R','R']
type_6 = ['B','B','C','B','A','R','R']

Rule_list = ['1','5','3','2','6','4']
