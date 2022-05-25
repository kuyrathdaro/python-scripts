# Big O runtime complexity: O(n^2)
def insertion_sort(list):
    for i in range(1, len(list)):
        next_element = list[i]
        j = i - 1
        while j >= 0 and list[j] > next_element:
            list [j + 1] = list[j]
            j = j - 1
        list [j + 1] = next_element
    return list

list = [9, 21, 3, 17, 111, 27, 32]
list = insertion_sort(list)
print(list)