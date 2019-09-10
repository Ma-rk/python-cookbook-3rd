from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

print()
print()

for x in a:
    print(x)
for x in b:
    print(x)
