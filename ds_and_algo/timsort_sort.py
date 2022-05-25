# Big O runtime complexity: O(nlog2n)
def insertion_sort(list, left=0, right=None):
    if right is None:
        right  = len(list) - 1

    for i in range(left + 1, right + 1):
        next_element = list[i]
        j = i - 1

        while j >= left and list[j] > next_element:
            list [j + 1] = list[j]
            j = j - 1

        list[j + 1] = next_element

    return list

def timsort(list):
    min_run = 32
    n = len(list)

    for i in range(0, n, min_run):
        insertion_sort(list, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_list = list[start:midpoint + 1] + list[midpoint + 1:end + 1]
            list[start:start + len(merged_list)] = merged_list
        size  = size * 2

    return list

list = [10, 3, 2, 32, 27, 100, 1]
list = timsort(list)
print(list)

