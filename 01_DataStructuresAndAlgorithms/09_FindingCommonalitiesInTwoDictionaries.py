# 두 딕셔너리의 유사점 찾기
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

keys_in_common = a.keys() & b.keys()
print('keys_in_common: {}'.format(keys_in_common))

keys_in_a_but_not_b = a.keys() - b.keys()
print('keys_in_a_but_not_b: {}'.format(keys_in_a_but_not_b))

items_in_common = a.items() & b.items()  # 같은 key/value를 가지는 원소.
print('items_in_common: {}'.format(items_in_common))

# a에서 특정 key가 제거된 c를 만들기.
c = {key: a[key] for key in a.keys() - {'x', 'y'}}
print(c)
