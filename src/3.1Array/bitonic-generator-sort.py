# Link: https://www.geeksforgeeks.org/sort-even-placed-elements-increasing-odd-placed-decreasing-order/

# Python3 Program to sort even-placed elements in increasing and
# odd-placed in decreasing order with constant space complexity
def bitonicGenerator(arr, n):
    # first odd index
    i = 1

    # last index
    j = n - 1

    # if last index is odd
    if (j % 2 != 0):
        # decrement j to even index
        j = j - 1

    # swapping till half of array
    while (i < j):
        arr[j], arr[i] = arr[i], arr[j]
        i = i + 2
        j = j - 2

    arr_f = []
    arr_s = []

    for i in range(int((n + 1) / 2)):
        arr_f.append(arr[i])

    i = int((n + 1) / 2)
    while (i < n):
        arr_s.append(arr[i])
        i = i + 1

    # Sort first half in increasing
    arr_f.sort()

    # Sort second half in decreasing
    arr_s.sort(reverse=True)

    for i in arr_s:
        arr_f.append(i)

    return arr_f


# Driver Program
arr = [1, 5, 8, 9, 6, 7, 3, 4, 2, 0]
n = len(arr)
arr = bitonicGenerator(arr, n)
print(arr)
