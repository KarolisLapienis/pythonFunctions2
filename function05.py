# *args priima betkiek parametru

list1 = [4, 8, 7, 9, 11]
list2 = [5, 8, -1, 25, 11, 45]

def skaiciuotiLyginiuNariuSuma(*args):
    sum = 0
    for i in args:
        if i % 2 == 0:
            sum += i
            print(i)
    return sum

print(skaiciuotiLyginiuNariuSuma(*list1, *list2, 12))
