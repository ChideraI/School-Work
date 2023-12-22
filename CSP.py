
def sudoku_board():
    list = []
    unsolvedSu = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.. "
    newSu = unsolvedSu.split(".")
    #newSu.append(list[i])
    for i in newSu:
        newSu2 = list.append(i)

def solve(sudoku_board):
    find = if_empty(sudoku_board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(sudoku_board, i, (row, col)):
            sudoku_board[row][col] = i

            if solve(sudoku_board):
                return True

            sudoku_board[row][col] = 0

    return False

def is_valid(sudoku_board, num, position):
    # Check row
    for i in range(len(sudoku_board[0])):
        if sudoku_board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(sudoku_board)):
        if sudoku_board[i][position[1]] == num and position[0] != i:
            return False

    # Check box
    x = position[1] // 3
    y = position[0] // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x * 3, x*3 + 3):
            if sudoku_board[i][j] == num and (i,j) != position:
                return False

    return True

def if_empty(sudoku_board):
    for i in range(len(sudoku_board)):
        for j in range(len(bo[0])):
            if sudoku_board[i][j] == 0:
                return (i, j)  # row, col

    return None

if __name__ == "__main__":

  sudoku_board()
