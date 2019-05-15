from operator import itemgetter
from itertools import groupby

# 필드별로 레코드 묶기

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

print(rows)
rows.sort(key=itemgetter('date'))
print(rows)

# 주의: itertools.groupby() 를 사용하기 전에 정렬할 시퀀스가 정렬돼 있어야 한다
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    print('  ', items)
    for i in items:
        print('    ', i)

print()
print()

# 1-6에 나온 defaultdict 를 사용해도 된다
from collections import defaultdict

# 메모리를 좀 더 많이 사용하지만 정렬한 후에 groupby()를 사용하는 것보다 빠르다
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for row in rows_by_date['07/02/2012']:
    print(row)
