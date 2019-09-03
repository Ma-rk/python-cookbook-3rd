from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('sample.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'yarl' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

f = open('sample.txt')
lines = linehistory(f)
next(lines)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#     TypeError: 'linehistory' object is not an iterator

# Call iter() first, then start iterating
it = iter(lines)
next(it)
next(it)
