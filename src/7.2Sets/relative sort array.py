def relativeSortArray(arr1, arr2):
    # result, the sorted array.
    result = []
    # sort arr1, so any elements not in arr2 can be appended to results in ascending order.
    arr1 = sorted(arr1)
    # set to check any elements in arr1 left out of arr2.
    arr2set = set(arr2)
    # go through all elements in arr2, for every element in arr2, append all matching elements from arr1.
    for a in arr2:
        for b in arr1:
            if a == b:
                result.append(b)
    # append remaining elements from arr1 not in arr2, in ascending order.
    for n in arr1:
        if n not in arr2set:
            result.append(n)
    # return result.
    return result