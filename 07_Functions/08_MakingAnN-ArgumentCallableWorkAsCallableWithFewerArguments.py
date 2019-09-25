import math
from functools import partial

from toolz import curry

# introducing partial

def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)
s1(2, 3, 4) # partial(1, 2, 3, 4)
s1(4, 5, 6)
s2 = partial(spam, d=42)
s2(1, 2, 3)
s2(4, 5, 6)
s3 = partial(spam, 1, 2, d=42)
s3(3)
s3(4)
s3(5)

pt = (4, 3)


# first way: using partial
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


points_1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
points_1.sort(key=partial(distance, pt))
print(points_1)


# first way: writing another function
def distance_2(p2):
    return distance(pt, p2)


points_2 = [(1, 2), (3, 4), (5, 6), (7, 8)]
points_2.sort(key=distance_2)
print(points_2)

# third way: using lambda
points_3 = [(1, 2), (3, 4), (5, 6), (7, 8)]
points_3.sort(key=lambda p: distance(pt, p))
print(points_3)
