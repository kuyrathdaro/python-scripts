# find array diff between two arrays
def array_diff(a, b):
    return [x for x in a if x not in b]