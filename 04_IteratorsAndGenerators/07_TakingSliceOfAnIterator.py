import time
import itertools


def count(n):
    while True:
        yield n
        n += 1
        if 10 < n:
            break


c = count(0)
#
# for cc in c:
#     time.sleep(0.1)
#     print(cc)

for x in itertools.islice(c, 2, 17):
    print(f'x: {x}')
