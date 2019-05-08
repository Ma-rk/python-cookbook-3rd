# 슬라이스에 이름 붙이기

#         0123456789012345678901234567890123456789012345678901234567890'
record = 'a...................100          .......513.25   ..........'

shares = int(record[20:33])
price = float(record[40:49])
cost1 = shares * price
print(cost1)

SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost2 = int(record[SHARES]) * float(record[PRICE])
print(cost2)

items = [0, 1, 2, 3, 4, 5, 6]
print(items)
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)
