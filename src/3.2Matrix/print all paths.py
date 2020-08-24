# https://www.techiedelight.com/find-all-paths-from-source-to-destination-in-matrix/
def findPaths(mat, path, i, j):
    
	(M, N) = (len(mat), len(mat[0]))

	# if we have reached the last cell, print the route
	if i == M - 1 and j == N - 1:
		print(path + [mat[i][j]])
		return

	# include current cell in path
	path.append(mat[i][j])

	# move right
	if 0 <= i < M and 0 <= j + 1 < N:
		findPaths(mat, path, i, j + 1)

	# move down
	if 0 <= i + 1 < M and 0 <= j < N:
		findPaths(mat, path, i + 1, j)

	# remove current cell from path
	path.pop()


if __name__ == '__main__':

	mat = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]

	path = []

	# start from (0, 0) cell
	x = y = 0

	findPaths(mat, path, x, y)
