# grieztas funkcijos parametru aprasymas :)


def datosFormatas(*, diena:int, menuo:str) -> str:
    return f'dabar yra {menuo[:-1]+"o"} men. {diena} diena'

print(datosFormatas(diena=13, menuo='Spalis'))
# print(datosFormatas('rugsejis', '13'))


