
def add5(x):
    return x + 5

def isodd(x):
    return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)
# if the function for the element is true,add it to the list,otherwise filter it out
b = list(filter(isodd, a))
print(b)
c = list(map(add5, filter(isodd, a)))
print(c)