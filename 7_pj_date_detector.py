import re
import datetime

# need to find dates in DD/MM/YYYY format
# d 01-31
# m 01-12
# y 1000-2999
# store into day, month, year variables

s = """
yes
20/11/1992
01/01/2020

no
AA/11/1992
20/BB/1992
20/11/CCCC
20 11 1992
20-11-1992

yes but fake date
45/45/2050
"""
L = s.split('\n')
L.pop(0)
print(L)

r = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
for l in L:
    mo = r.search(l)
    try:
        print(f'the entire expression in {mo.group(0)}')
        day = mo.group(1)
        month = mo.group(2)
        year = mo.group(3)
        print(f'the day is {day}')
        print(f'the month is {month}')
        print(f'the year is {year}')
        # write additional code to detect if the date is real
        try:
            datetime.datetime(int(year), int(month), int(day))
        except:
            print('no such date')
        else:
            print('the date exists')
    except:
        print('no such ding')
