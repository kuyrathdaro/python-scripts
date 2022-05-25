# Big O runtime complexity: O(logn)
# Make sure the list is sorted
def binary_search(sorted_list, value):
    i = 0
    start = 0
    end = len(list) - 1

    while i < len(list):
        middle = (start + end) // 2

        if sorted_list[middle] == value:
            return True
        elif sorted_list[middle] < value:
            start = middle + 1
        elif sorted_list[middle] > value:
            end = middle - 1
        i = i + 1

    return False

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(list, 4))
print(binary_search(list, 11))
