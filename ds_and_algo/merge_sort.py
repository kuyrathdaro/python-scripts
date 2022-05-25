# Big O runtime complexity: O(nlog2n)
def merge(left, right):
    if len(left) == 0:
        return right
    
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(list):
    if len(list) < 2:
        return list
    
    midpoint = len(list) // 2

    return merge(left=merge_sort(list[:midpoint]), right=merge_sort(list[midpoint:]))

list = [9, 3, 2, 1, 5, 111, 32]
list = merge_sort(list)
print(list)