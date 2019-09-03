a = [1, 2, 3, 4]
for x in a:
    print(x)
for x in reversed(a):
    print(x)

# Reversed iteration only works if the object in question has a size
# that can be determined
# or if the object implements a __reversed__() special method.
# If neither of these can be satisfied, you’ll have to convert the object into a list first.
# Print a file backwards
f = open('sample.txt')
for line in reversed(list(f)):
    print(line, end='')


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
        n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
        n += 1
