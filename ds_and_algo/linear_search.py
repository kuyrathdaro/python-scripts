# Big O runtime complexity: O(n)
def linear_search(list, value):
    search_at = 0
    search_res = False

    while search_at < len(list) and search_res is False:
        if list[search_at] == value:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res

list = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(list, 12))
print(linear_search(list, 91))