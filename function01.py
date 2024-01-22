# Rasti eilutes mediana

list1 = [4, 8, 7, 9, 11]
list2 = [5, 8, -1, 25, 11, 45]

def findMedian(list):
    list.sort()
    lenList = len(list)

    if lenList % 2 != 0 :
        median = list[lenList // 2]
    else:
        median = (list[lenList//2] + list[lenList//2 -1])
    return list, median


print(f'{list.sort(list1)} mediana: {findMedian(list1)}')
print(list1)