from collections import Counter

c1 = Counter('gallad')
c2 = Counter(["a", "a", "b", "c", "c"])
c3 = Counter({"a":1, "b":2})
c4 = Counter(cats=4, dogs=7)
print(c1)
print(c2)
print(c3)
print(c4)
print(list(c1.elements()))
print(c2.most_common(3))

d = Counter(a=4, b=2, c=0, d=-2)
d1 = Counter(['a', 'b', 'b', 'c'])

d.subtract(d1)
print(d)
d.update(d1)
print(d)
#d.clear()
print(d)
print(d-d1)
print(d & d1)