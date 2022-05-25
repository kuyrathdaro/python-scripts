# Big O runtime complexity: O(n^2)
def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

list = [19, 2, 31, 45, 30, 11, 127, 27]
list = selection_sort(list)
print(list)