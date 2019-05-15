from operator import itemgetter

# 일반 키로 딕셔너리 리스트 정렬

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_lname = sorted(rows, key=itemgetter('lname'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_lname)
print(rows_by_lfname)
print(rows_by_uid)

# itemgetter 대신 lambda를 쓸 수도 있지만 itemgetter가 좀 더 빠르다
rows_f_lambda = sorted(rows, key=lambda row: row['fname'])
rows_l_lambda = sorted(rows, key=lambda row: row['lname'])
rows_lf_lambda = sorted(rows, key=lambda row: (row['lname'], row['fname']))
rows_uid_lambda = sorted(rows, key=lambda row: row['uid'])

print(rows_f_lambda)
print(rows_l_lambda)
print(rows_lf_lambda)
print(rows_uid_lambda)

# itemgetter는 min(), max() 에도 사용할 수 있다
min_row = min(rows, key=itemgetter('uid'))
print(min_row)
max_row = max(rows, key=itemgetter('uid'))
print(max_row)
