# 1-1 시퀀스를 개별 변수로 나누기

p = (4, 5)
x, y = p
print(x)
print(y)

data = ['Ma-rk', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

name, shares, price, (year, month, day) = data
print(name)
print(shares)
print(price)
print(year)
print(month)
print(day)

s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)

_, shares_, price_, (_, _, day_) = data
print(shares_)
print(price_)
print(day_)
