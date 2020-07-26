# Link: 
# IsDone: 0
class CamptureRegions:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) == 0:
            return
        for row in range(0, len(board)):
            self.mark(board, row, 0)
            self.mark(board, row, len(board[0]) - 1)
        for col in range(0, len(board[0])):
            self.mark(board, 0, col)
            self.mark(board, len(board) - 1, col)
        
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == '$':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'
        
    def mark(self, board, row, col):
        stack = []
        nCols = len(board[0])
        stack.append(row * nCols + col)
        while len(stack) > 0:
            position = stack. pop()
            row = position // nCols
            col = position % nCols
            if board[row][col] != 'O':
                continue
            board[row][col] = '$'
            if row > 0:
                stack.append((row - 1) * nCols + col)
            if row < len(board) - 1:
                stack.append((row + 1) * nCols + col)
            if col > 0: 
                stack.append(row * nCols + col - 1)
            if col < nCols - 1:
                stack.append(row * nCols + col + 1)
