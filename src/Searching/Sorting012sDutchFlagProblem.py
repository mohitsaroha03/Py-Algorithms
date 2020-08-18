# Link: 
# IsDone: 0
def sorting012sDutchFlagProblem(A):
    n = len(A)
    zero = 0; two = n - 1
    # Write 1 at the beginning; 2 at the end.
    cur = 0
    while cur <= two:
        print cur, A, zero, two
        if A[cur] == 0:
            if cur > zero:
                A[zero], A[cur] = A[cur], A[zero]
                zero += 1
            else:  # TRICKY PART.
                # cur == zero and A[cur] == A[zero] == 0
                cur += 1
                zero += 1
        
        elif A[cur] == 2:
            if cur < two:
                A[two], A[cur] = A[cur], A[two]
                two -= 1
            else:
                break
        else:
            cur += 1
    print A, '\n'
    return A

if __name__ == '__main__':
    sorting012sDutchFlagProblem([2, 0, 1, 0, 2, 1, 2, 2, 1, 1])
    sorting012sDutchFlagProblem([2, 1, 2, 1, 2, 0])
    sorting012sDutchFlagProblem([0, 0, 1, 2, 2, 2, 0, 0, 0])
