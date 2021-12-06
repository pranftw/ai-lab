from copy import deepcopy
import math

def get_board():
    board = []
    for i in range(3):
        new_row = []
        for j in range(3):
            while(True):
                try:
                    val = int(input(f"Enter [{i}][{j}]: "))
                    if(val in range(1,9) or val==-1):
                        new_row.append(val)
                        break
                except:
                    pass
                print("Enter valid input! Try again!")
        board.append(new_row)

def validate_board(board):
    count = []
    for _ in range(9):
        count.append(0)
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==-1):
                count[0]+=1
            else:
                count[board[i][j]]+=1
    for c in count:
        if(c==0 or c>1):
            return False
    return True

def push(s,new_board_state):
    s.append(new_board_state)

def pop(s):
    return s.pop(-1)

def check(goal_board,board):
    return goal_board==board

def print_board(board):
    print()
    for i in range(len(board)):
        print(f"{board[i][0]}\t{board[i][1]}\t{board[i][2]}")
    print()

def get_empty_idx(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==-1):
                return (i,j)

def get_all_possibilities(board):
    i,j = get_empty_idx(board)
    possibilities = []
    if(i-1>=0):
        board_x = deepcopy(board)
        board_x[i][j] = board_x[i-1][j]
        board_x[i-1][j] = -1
        possibilities.append(board_x)
    if(i+1<len(board)):
        board_x = deepcopy(board)
        board_x[i][j] = board_x[i+1][j]
        board_x[i+1][j] = -1
        possibilities.append(board_x)
    if(j-1>=0):
        board_x = deepcopy(board)
        board_x[i][j] = board_x[i][j-1]
        board_x[i][j-1] = -1
        possibilities.append(board_x)
    if(j+1<len(board)):
        board_x = deepcopy(board)
        board_x[i][j] = board_x[i][j+1]
        board_x[i][j+1] = -1
        possibilities.append(board_x)
    return possibilities

def solve(goal_board, initial_board_state):
    max_depth = 0
    while(True):
        visited = []
        s = [deepcopy(initial_board_state)]
        depth = [0]
        i = 0
        while(depth[i]<=max_depth):
            board = s[i]
            visited.append(board)
            curr_depth = depth[i]
            possibilities = get_all_possibilities(board)
            for p in possibilities:
                if(p not in visited):
                    push(s,p)
                    push(depth,curr_depth+1)
            i+=1
        while(len(s)!=0):
            board = pop(s)
            curr_depth = pop(depth)
            print_board(board)
            if(check(goal_board,board)):
                print(f"Solved at depth {curr_depth}!")
                print_board(board)
                return
        max_depth+=1

if __name__=='__main__':
    goal_board = [[1,2,3],[4,5,6],[7,8,-1]]
    # board = get_board()
    board = [[1,2,3],[-1,4,6],[7,5,8]]
    if(not(validate_board(board))):
        print("Invalid board elements! Try again!")
        exit()
    solve(goal_board,board)