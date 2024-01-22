# sorted vs sort

sar = [5, 8, 9, 4, 7, 1, -2, 8]

# sar.sort()
# print(sar)

sortedSar = sorted(sar)
print(sortedSar)
print(sar)

numTuple = (5, 7, 9, 7, -1)

print(sorted(numTuple))  # sorted konvertuoja i sarasa

sortedTuple = tuple(sorted(numTuple))
print(sortedTuple)

numSet = {5, 5, 10, 1, 0}
print(numSet)
print(sorted(numSet))
print(set(sorted(numSet)))  # aibeje nera tvarkos, del to ji pasidaro nebesurikiuota

print(sorted(sar, reverse=True))


cars = ['BMW', 'Ford', 'Opel', 'Tesla', 'Mercedes', 'Suzuki', 'Subaru', 'Volvo', 'Sabaru', 'Aabaru']
print(sorted(cars))
print(sorted(cars, key=len))

def kiekPriebalsiu(sar):
    balses = ['a', 'e', 'i', 'o', 'u', 'y']
    kiek = 0
    for raide in sar:
        if raide.lower() not in balses:
            kiek += 1
    return kiek

print(sorted(cars, key=kiekPriebalsiu))

