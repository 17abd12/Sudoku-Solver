from copy import deepcopy
from Gui import display_sudoku

    
board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
            
def termination(board):
    for x in board:
        for y in x:
            if y == ".":
                return False
    else:
        return True
def action(board,i,j):
    result = [str(x) for x in range(1,10)]
    if board[i][j] != '.':
        return []
    for x in range(0,9):
        # for checking the whole row
        if board[i][x] != '.':
            if board[i][x] in result:
                result.remove(board[i][x])
        # for checking the whole column
        if board[x][j] != '.':
            if board[x][j] in result:
                result.remove(board[x][j])
        # for checking other half
    z,s = (i // 3) * 3,(j // 3) * 3
    for r in range(z,z + 3):
            for q in range(s,s + 3):
                if board[r][q] != '.':
                    if board[r][q] in result:
                        result.remove(board[r][q])         
    return result

def recursive(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                possible_actions = action(board,i,j)
                for x in possible_actions:

                    result = False
                    board[i][j] = x
                    if termination(board):
                        print('The Board Has Ended')
                        return True
                    else:
                       result =  recursive(board)

                    if result:
                        return True
                else:
                    print('No Such solution')
                    board[i][j] = '.'
                    return False

display_sudoku(board,board,'Sudoku Unsolved')
b = deepcopy(board)
recursive(board)
display_sudoku(board,b,'Soduko Solved')