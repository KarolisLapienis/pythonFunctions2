list1 = [5, 8, 9, -1, 25, 11, 7, 9]

rez = map(lambda x: 'Nelyginis' if x % 2 != 0 else 'Lyginis', list1)

print(list(rez))

list3 = [5, 8, 7, 4, 17]
list4 = [11, 4, 12, 5, 9]
# gauti sarasa5 kur elementai yra x+y jei x<y ir x-y jei x>y

list5 = list(map(lambda x, y: x-y if x>y else x+y, list3, list4 ))

print(list5)