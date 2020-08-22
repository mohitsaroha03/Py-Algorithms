# Link - https://www.geeksforgeeks.org/distance-nearest-cell-1-binary-matrix/

# Python3 program to find distance of
# nearest cell having 1 in a binary matrix.

# Prthe distance of nearest cell
# having 1 for each cell.
def printDistance(mat):
    global N, M
    ans = [[None] * M for i in range(N)]

    # Initialize the answer matrix
    # with INT_MAX.
    for i in range(N):
        for j in range(M):
            ans[i][j] = 999999999999

    # For each cell
    for i in range(N):
        for j in range(M):

            # Traversing the whole matrix
            # to find the minimum distance.
            for k in range(N):
                for l in range(M):

                    # If cell contain 1, check
                    # for minimum distance.
                    if (mat[k][l] == 1):
                        ans[i][j] = min(ans[i][j],
                                        abs(i - k) + abs(j - l))

                    # Printing the answer.
    for i in range(N):
        for j in range(M):
            print(ans[i][j])
        print()

    # Driver Code


N = 3
M = 4
mat = [[0, 0, 0, 1],
       [0, 0, 1, 1],
       [0, 1, 1, 0]]

printDistance(mat)
