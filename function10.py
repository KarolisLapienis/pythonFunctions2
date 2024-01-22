# filter 

sar = [8, 7, 4, 7, 9, 11, 13, 12]

def arLyginis(n):
    return n % 2 == 0

lyginiai = list(filter(arLyginis, sar))
print(lyginiai)

nelyginiuSar = list(filter(lambda n: n % 2 !=0, sar))

print(nelyginiuSar)

cars = ['BMW', 'Ford', 'Opel', 'Tesla', 'Mercedes', 'Suzuki', 'Subaru', 'Volvo', 'Sabaru', 'Aabaru']

print(max(cars))

print(max(cars, key = lambda car: len(car)))