
from collections import namedtuple

Point = namedtuple("Point", 'x y z')
newPoint = Point(3, 4, 5)
print(newPoint)
print(newPoint._fields)
newPoint = newPoint._replace(y=6)
print(newPoint)

p2 = Point._make(['a', 'b', 'c'])
print(p2)