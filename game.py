# tic tac toee game that player win when they have k X or O in a row, column or diagonal
rowNum = int(input("Enter the number of rows: "))
colNum = int(input("Enter the number of columns: "))
k = int(input("Enter the number of k: "))

board = []
for i in range(rowNum):
    board.append([])
    for j in range(colNum):
        board[i].append(-1)

# function that get submatrix of board to implement alphabet prunc algorithm
# choose submatrix depend on posibility of win or lose
def getSubMatrix(board, rowNum, colNum):
    subMatrix = []
    for i in range(rowNum):
        subMatrix.append([])
        for j in range(colNum):
            subMatrix[i].append(board[i][j])
    return subMatrix