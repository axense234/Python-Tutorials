
def func(x):
    return x + 5

print(func(2))
# basically if you only need to return a line,use lambda
func2 = lambda x: x+5
print(func2(2))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = list(map(lambda x: x+30, a))
print(newlist)
newlist = list(filter(lambda x: x%2 == 0, a))
print(newlist)