def spam(a, b=42):
    print(a, b)


spam(1)  # Ok. a=1, b=42
spam(1, 2)  # Ok. a=1, b=2


# Using a list as a default value
def spam_2(a, b=None):
    if b is None:
        b = []


_no_value = object()


def spam_3(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


x = 42


def spam_4(a, b=x):
    print(a, b)


print(spam(1))  # 1 42
x = 23
print(spam(1))  # 1 42
