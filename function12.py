txt = 'Globali sritis'

def fun1():
    txt = 'Enclosing sritis'

    def fun2():
        txt = 'Lokali sritis'
        print(f'fun2 {txt}')
    fun2()
    print(f'fun1 {txt}')
    return txt

print(txt)
fun1()