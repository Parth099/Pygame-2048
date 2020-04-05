#2048 in snap
#https://snap.berkeley.edu/snap/snap.html#present:Username=parth099&ProjectName=2048%20-%20SNAP
import random
global moves
global score
score = 0
moves = ["", " "]

def genBoard():
    global board
    board = [[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    drop_two(board)

    return board

def combine_lr(board, t1, t2):
    global score
    if board[t1[0]][t1[1]] == board[t2[0]][t2[1]]:
        board[t1[0]][t1[1]]*=2
        board[t2[0]][t2[1]]= 0  
        score+=(board[t1[0]][t1[1]])

def check_open(board, coord):
    if board[coord[0]][coord[1]] == 0:
        return True
    else:
        return False 

def swap_lr(board,idx1, idx2, row):
    a = board[row][idx1]
    board[row][idx1] =board[row][idx2]
    board[row][idx2] = a

def drawBoard(board):  #Beta test ONLY
    for i in range(0, 4):
        print(board[i])

def shift_right(board): #if and only if 0<=col<=3
    for x in range(0, 2):
        for row in range(0, 4):
            for i in range(0, 3):
                if check_open(board,(row, i+1)):
                    swap_lr(board, i, i+1, row)

                t2 = (row, i)
                t1 = (row, i+1)
                combine_lr(board, t1, t2)
    moves.append("r")

def shift_left(board): 
    for x in range(0, 2):
        for row in range(0, 4):
            for i in range(3, 0, -1):
                if check_open(board,(row, i-1)):
                    swap_lr(board, i, i-1, row)

                t1 = (row, i-1)
                t2 = (row, i)
                combine_lr(board, t1, t2)
    moves.append("l")

def swap_ud(board, idx1, idx2, col): #(b, 0 , 1, 1)
    a = board[idx1][col]
    board[idx1][col] = board[idx2][col]
    board[idx2][col] = a


def shift_up_col(board, col):
    for k in range(1, 4):
        t1 = (k-1, col)
        t2 = (k, col)
        combine_lr(board, t1, t2)   #combines t1 and deletes t2 #check passed
    for i in range(0, 3):
        if check_open(board,(i, col)):  #just is a oneline boolean if k == 0 or not
            board[i][col] = board[i+1][col] 
            board[i+1][col] = 0
    

def shift_down_col(board, col):
    for k in range(0, 3):
        t1 = (k+1, col)
        t2 = (k  , col)
        combine_lr(board, t1, t2)
    for i in range(0, 3):
        if check_open(board,(i+1, col)):
            board[i+1][col] = board[i][col]
            board[i][col] = 0

def shift_up(board):
    for r in range(0, 3):
        for col in range(0, 4):
            shift_up_col(board, col)
    moves.append("u")

def shift_down(board): 
    for r in range(0, 2):
        for col in range(0, 4):
            shift_down_col(board, col)
    moves.append("d")

def drop_two(board):
    open_spot = False
    dropped = False
    if (moves[len(moves)-1] != moves[len(moves)-2]):
        for row in range(4):
            for col in range(4):
                if board[row][col] == 0:
                    open_spot = True 
        while ((not dropped) and open_spot):
            a = random.randint(0, 3)
            b = random.randint(0, 3)
            if board[a][b] == 0:
                board[a][b] = 2
                dropped = True

def get_score():
    return score

def rotate_90(matrix):
    assert (len(matrix) * len(matrix[0])) % 2 == 0 , "Trying to reflect a non_square matrix"
    n = len(matrix[0])
    for x in range(0, n):
        for y in range(x, n):
            t = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = t

def print_board(b):
    for row in range(len(b)):
        print(b[row])
    print('___________')
             
def Alpha_test_driver():
    board = genBoard()
    drop_two(board)
    drawBoard(board)
    print("____________")
    key_pressed = ""
    while (key_pressed.lower() != "quit"):
        key_pressed = str(input(">: "))
        print("")
        if key_pressed.lower() == "up":
            shift_up(board)
            drop_two(board)
        elif key_pressed.lower() == "down":   
            shift_down(board)
            drop_two(board)
        elif key_pressed.lower() == "left":
            shift_left(board)
            drop_two(board)
        elif key_pressed.lower() == "right":    
            shift_right(board)
            drop_two(board)
        else:
            if key_pressed.lower() != "quit":
                print("Err retry")
            else: 
                pass
         
        drawBoard(board)
        print("____________")
        print(score)
        print("____________")

def main():
    Alpha_test_driver()

if __name__ == "__main__":
    main()