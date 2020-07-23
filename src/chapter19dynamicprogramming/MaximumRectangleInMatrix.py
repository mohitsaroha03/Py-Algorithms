# isGFG: , Link: 
# IsDone: 0
def maximumRectangleInMatrix(self, matrixInput):
	maxArea = 0
	rows = []
	columns = []
	for i in range(0, len(matrixInput)):
	    rowTemp = []
	    colTemp = []
	    for j in range(0, len(matrixInput[0])):
		rowTemp.append(0)
		colTemp.append(0)
	    rows.append(rowTemp)
	    columns.append(colTemp)
		
	for i in range(len(matrixInput) - 1, -1, -1):
	    for j in range(len(matrixInput[0]) - 1, -1, -1):
		area = 0
		if matrixInput[i][j] == '1':
		    if i == len(matrixInput) - 1:
			rows[i][j] = 1
		    else:
			rows[i][j] = rows[i + 1][j] + 1
		    if j == len(matrixInput[0]) - 1:
			columns[i][j] = 1
		    else:
			columns[i][j] = columns[i][j + 1] + 1
		    area = columns[i][j]
		    minCol = columns[i][j]
		for k in range(1, rows[i][j]):
		    if minCol > columns[i + k][j]:
			minCol = columns[i + k][j]
		    if (k + 1) * minCol > area:
			area = (k + 1) * minCol
		if maxArea < area:
		    maxArea = area
	return maxArea
