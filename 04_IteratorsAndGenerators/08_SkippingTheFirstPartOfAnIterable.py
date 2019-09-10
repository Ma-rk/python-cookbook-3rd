from itertools import dropwhile

with open('sample.txt') as f:
    for line in f:
        print(line, end='')

print()
print()
print()
print('========using drop while========')
with open('sample.txt') as f:
    for line in dropwhile(lambda line: line.startswith('pip'), f):
        print(line, end='')


print()
print()
print()
print('========a good try========')
with open('sample.txt') as f:
    lines = (line for line in f if not line.startswith('pip'))
    for line in lines:
        print(line, end='')
