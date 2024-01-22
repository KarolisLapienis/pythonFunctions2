x = 5
def fun1():
    global x  # to geriau nedaryti
    x = 10
    print(x)

fun1()
print(x)

def fun4():
    x = 100
    return x

a = fun4()  # perteklinis ir nerekomenduojamas

def fun5():
    print(fun4())

fun5()

