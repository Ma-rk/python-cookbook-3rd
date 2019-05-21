from collections import namedtuple

# 시퀀스 요소에 이름 매핑

# 위치에 대한 인덱스로 요소에 접근하는 코드를
# 요소의 인덱스가 아닌 이름으로 접근하도록 고치고 싶을때
Subscriber = namedtuple('Subscriber', ['email', 'joined'])
sub = Subscriber('mark@mark.com', '2019-05-21')

print('sub')
print(sub)
print(sub.email)
print(sub.joined)

Stock = namedtuple('Stock', ['name', 'share', 'price'])
records = [
    Stock('ACME', 20, 45.23),
    Stock('AAPL', 20, 612.78),
    Stock('IBM', 20, 205.55),
    Stock('HPQ', 20, 37.20),
    Stock('FB', 20, 10.75)
]

print()
print('example')


def compute_cost_1(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


def compute_cost_2(records):
    total = 0.0
    for rec in records:
        total += rec.share * rec.price
    return total


print(compute_cost_1(records))
print(compute_cost_2(records))

# namedtuple 를 수정하는 방법
s = Stock('ACME', 20, 45.23)
print(s)
# s.name = 'not_ACME' <- 이 코드는 AttributeError가 난다

s = s._replace(name='not_ACME')
print(s)

print()
print('assign not every field')
# 지금까지와 같은 방법으로는 항상 모든 필드에 값을 명시해야만 객체를 생성할 수 있다.
# 값 할당을 원하는 필드에만 값을 표시해서 객체를 생성하는 방법:
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
new_a = dict_to_stock(a)
b = {'name': 'APPL', 'shares': 1000, 'price': 123.45, 'date': '2019-05-21'}
new_b = dict_to_stock(b)
print(a)
print(new_a)
print(b)
print(new_b)
