import pandas as pd
from datetime import datetime


def data_list(beginDate, endDate):
    date_l = [datetime.strftime(x, '%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l

if __name__ == '__main__':
a = ("20210101", "20211231")
begin = a[0]
end = a[1]
year_date_list = data_list(begin, end)
print(year_date_list)
print(len(year_date_list))
