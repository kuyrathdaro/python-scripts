# Big O runtime complexity: O(n^2)
def shell_sort(list):
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list)):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j = j - gap
            list[j] = temp
        gap = gap // 2

    return list

list = [9, 8, 3, 1, 2, 10, 32, 27]
list = shell_sort(list)
print(list)