list1 = [5, 8, 9, -1, 25, 11, 7, 9]

def arLyginis(sk):
    if sk % 2 == 0:
        ats = 'lyginis'
    else:
        ats = 'nelyginis'
    return ats

# def arLyginis(sk):
#     ats = 'nelyginis'
#     if sk % 2 == 0:
#         ats = 'lyginis'
#     return ats

rez = map(arLyginis, list1)

print(rez)
print(type(rez))
print(list(rez))

