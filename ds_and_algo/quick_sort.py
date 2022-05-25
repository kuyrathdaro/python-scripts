# Big O runtime complexity: O(nlog2n)
from random import randint

def quick_sort(list):
    if len(list) < 2:
        return list
    
    low, same, high = [], [], []

    pivot = list[randint(0, len(list) - 1)]

    for item in list:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quick_sort(low) + same + quick_sort(high)

list = [3, 2, 1, 7, 13, 32, 111, 100]
list = quick_sort(list)
print(list)