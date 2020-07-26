#

def rotateList(A, K):
    n = K % len(A)
    word = A[::-1]
    return A[n:] + word[len(A) - n:]
A = [7, 3, 2, 3, 3, 6, 3]
print A, rotateList(A, 3)
