x = 11111
def fun1():
    x = 22222
    def fun2():
        nonlocal x
        x = 33333
        print(f'fun2 : {x}')
    fun2()
    print(f'fun1 : {x}')

fun1()
print(x)