from collections import deque

d = deque("hello")
d1 = deque('hello', maxlen=5)
print(d)
d.append('4')
d.appendleft(5)
print(d)
d.popleft()
print(d)
# d.clear()
# print(d)
d.extend('456')
print(d)
d.extend('hello')
print(d)
d.extendleft('hey')
print(d)
d.rotate(-1100)
print(d)
d1.append("hey")
print(d1)