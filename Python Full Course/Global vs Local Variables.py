
var = 5
loop = True

def func(x):
    global loop
    loop = 7
    if x == 5:
        return loop


def anotherfunc():
    newVar = 5
    print(newVar)

anotherfunc()