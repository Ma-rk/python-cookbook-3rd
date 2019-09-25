# introducing lambda

add = lambda x, y: x + y
print(add(2, 3))


def add_2(x, y):
    return x + y


print(add_2(2, 3))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
sorted_names_1 = sorted(names, key=lambda name: name.split()[-1].lower())
print(sorted_names_1)


def get_lowered_list_name(before_name):
    return before_name.split()[-1].lower()


sorted_names_2 = sorted(names, key=get_lowered_list_name)
print(sorted_names_2)
