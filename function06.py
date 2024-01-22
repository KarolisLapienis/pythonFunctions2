# kas yra **kwargs


# komandaA = {'Algis' : 25, 'Jonas' : 17, 'Petras' : 22}

# print(komandaA)

def taskuSkaiciavimas(**kwargs):
    suma = 0
    didziausias = 0
    for k, v in kwargs.items():
        print(f'zaidejas {k} surinko {v} tasku')
        suma += v
        if v > didziausias:
            didziausias = v
    return suma, didziausias

# print(komandaA)



print(taskuSkaiciavimas(Algis = 25, Jonas = 17, Petras = 22, Tadas = 55))