# Big O runtime complexity: O(n^2)
def bubble_sort(list):
    for iter_num in range(len(list)-1, 0, -1):
        for i in range(iter_num):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

    return list

list = [3, 2, 1, 30, 27, 111, 110]
list = bubble_sort(list)
print(list)