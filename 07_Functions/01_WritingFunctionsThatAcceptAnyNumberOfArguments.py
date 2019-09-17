print()
print('avg()')


def avg(first, *rest):
    # rest is a tuple of all the extra positional arguments passed
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3, 4))

import html

print()
print('make_element()')


def make_element(name, value, **attrs):
    keyvals = [f' {item_1}="{item_2}"' for item_1, item_2 in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))

print()
print('anyargs()')


def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict


anyargs('a', 'b', c='c', d='c')

print('a()')


def a(x, *args, y):
    print(x)
    print(args)
    print(y)


a('a', '1', '2', '3', y='y')

print('b()')


def b(x, *args, y, **kwargs):
    print(x)
    print(args)
    print(y)
    print(kwargs)


b('a', '1', '2', '3', y='y', kw1='kw1', kw2='kw2')
