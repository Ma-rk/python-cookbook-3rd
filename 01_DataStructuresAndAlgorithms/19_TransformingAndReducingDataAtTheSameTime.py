# 데이터 건 수 줄이기와 변환하기를 동시에 하기

# 정사각형 넓이의 합
nums = [1, 2, 3, 4, 5]

s1 = sum(x * x for x in nums)
print(s1)
s2 = sum([x * x for x in nums])
print(s2)

result_list = []
for num in nums:
    result_list.append(num * num)
s3 = sum(result_list)
print(s3)

# 디렉토리에 .py 파일이 하나라도 있는지 확인
import os

files = os.listdir('./')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry... no python.')

# 튜플을 csv로 출력
some_tuple = ('ACME', 50, 123.45)
print(','.join(str(x) for x in some_tuple))

# 필드의 값을 이용해 데이터 건 수를 줄임
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)
