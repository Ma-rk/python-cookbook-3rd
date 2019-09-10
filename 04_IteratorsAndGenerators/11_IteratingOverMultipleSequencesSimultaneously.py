# 여러 시퀀스에 들어있는 아이템을 동시에 순환하고 싶다.

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

print()
print()
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)

print()
print()
from itertools import zip_longest

for i in zip_longest(a, b):
    print(i)

print()
print()
for i in zip_longest(a, b, fillvalue=0):
    print(i)

    # 두 값을 묶어 딕셔너리로 만들 수 있다
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)

print()
print()
for name, val in zip(headers, values):
    print(name, '=', val)

print()
print()
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)
