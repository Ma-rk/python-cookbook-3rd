# 순서를 깨지 않고 시퀀스의 중복 없애기

a1 = [1, 5, 2, 1, 9, 1, 5, 10]
a2 = [{'x': 1, 'y': 2},
      {'x': 1, 'y': 3},
      {'x': 1, 'y': 2},
      {'x': 2, 'y': 4}]


def de_dupe_when_hashable(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def de_dupe_when_not_hashable(items, key=None):
    seen = set()
    for item in items:
        print('item: {}, key: {}, key(item): {}'.format(item, key, key(item)))
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def return_xy_tuple(item_dict: dict):
    return item_dict['x'], item_dict['y']


def return_x_tuple(item_dict: dict):
    return item_dict['x']


# 단순히 set()만 사용해도 중복이 제거되긴 하지만 순서가 보장되지 않는다
de_dupe_set = set(a1)
print(de_dupe_set)

# 순서를 보장하며 중복을 제거한다
print('de_dupe_when_hashable')
for gen_item in de_dupe_when_hashable(a1):
    print(gen_item)
print()
de_dupe_result = de_dupe_when_hashable(a1)
print(de_dupe_result)
de_dupe_list = list(de_dupe_when_hashable(a1))
print(de_dupe_list)

print()
print('de_dupe_when_not_hashable')
for gen_item in de_dupe_when_not_hashable(a2, key=lambda d: (d['x'], d['y'])):
    print(gen_item)
for gen_item in de_dupe_when_not_hashable(a2, key=return_xy_tuple):
    print(gen_item)
print()
for gen_item in de_dupe_when_not_hashable(a2, key=lambda d: (d['x'])):
    print(gen_item)
for gen_item in de_dupe_when_not_hashable(a2, key=return_x_tuple):
    print(gen_item)
