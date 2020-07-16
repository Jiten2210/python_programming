def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1;


def binary_search(a, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        if a[mid] == x:
            return mid

        elif a[mid] > x:
            return binary_search(a, low, mid - 1, x)
        else:
            return binary_search(a, mid + 1, high, x)
    else:
        return -1


x = 5
a = [1, 2, 5, 4, 3, 0]
print(linear_search(a, x))
print(binary_search(a, 0, len(a) - 1, x))
