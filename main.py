import random

def initialize_board():
    # Create an empty 9x9 Sudoku board filled with 0s.
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Define the number of filled cells in the initial puzzle.
    num_filled_cells = random.randint(10, 30)  # Adjust as needed.

    for _ in range(num_filled_cells):
        while True:
            # Randomly select a row and column.
            row, col = random.randint(0, 8), random.randint(0, 8)
            
            # Check if the selected cell is empty (has a value of 0).
            if board[row][col] == 0:
                break  # Valid empty cell found.

        # Randomly select a number (1 to 9) and fill the cell.
        num = random.randint(1, 9)
        board[row][col] = num

    return board
       
board=intialize_board()

def solve(bo):
    fnd=find(bo)
    if not fnd:
        return True
    else :
        row,col=fnd
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i
            if solve(bo):
                return True
            bo[row][col]=0
    return False

def valid(bo,num,pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and pos[1]!=i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[0]!=i:
            return False
    box_x=pos[1]//3
    box_y=pos[0]//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False
    return True

def display(bo):
    for i in range(len(bo)):
        if i % 3==0 and i!=0:
            print("- - - - - - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print(" | ",end=" ")
            if j==8:
                print(bo[i][j])
            else:
                print(bo[i][j],end=" ")

def find(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j)
    return None

display(board)
print("______________________________________________")
solve(board)
display(board)
