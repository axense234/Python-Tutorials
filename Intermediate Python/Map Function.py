
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x ** x
#map takes a function an applies it to every element of a list
print(list(map(func, li)))

print([func(x) for x in li if x%2 == 0])