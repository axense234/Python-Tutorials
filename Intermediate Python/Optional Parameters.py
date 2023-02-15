# default value,overwritten if wanted
def func(word, freq=1):
    print(word*freq)


call = func("tim", 5)
print(call)

def func2(word, add=5,freq=1):
    print(word*(freq+add))


call = func2("Nigger")
print(call)

