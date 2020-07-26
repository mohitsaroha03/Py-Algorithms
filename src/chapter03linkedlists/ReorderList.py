#

def oddeven(A):
    "Odd-Even sort implementation"
    sorted = False
    while(not sorted):
        sorted = True
        for i in range(1, len(A) - 1, 2):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                sorted = False
        for i in range(0, len(A) - 1, 2):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                sorted = False
        if not sorted:
            print A
