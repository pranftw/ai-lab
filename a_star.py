import math

"""
1 2 3    
4 5 6
7 8 -1

2 4 6
1 5 7
8 3 -1
"""

def check(goal_board, board):
    return goal_board==board

def get_orig_idx(val, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==val):
                return i,j

def get_hn(goal_board, board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board)):
            orig_idx_i,orig_idx_j = get_orig_idx(board[i][j],goal_board)
            sum+=math.sqrt(math.pow(orig_idx_i-i,2) + math.pow(orig_idx_j-j,2))
    return sum

def move(board, direction):
    empty_i,empty_j = get_orig_idx(-1,board)
    new_i,new_j = None,None
    if(direction==0 and empty_i-1>=0): # Up
        new_i,new_j = empty_i-1,empty_j
    elif(direction==1 and empty_i+1<len(board)): # Down
        new_i,new_j = empty_i+1,empty_j
    elif(direction==2 and empty_j-1>=0): # Left
        new_i,new_j = empty_i,empty_j-1
    elif(direction==3 and empty_j+1<len(board)): #Right
        new_i,new_j = empty_i,empty_j+1
    if(new_i is not None and new_j is not None):
        board[empty_i][empty_j] = board[new_i][new_j]
        board[new_i][new_j] = -1
    return board

def print_board(board):
    for i in range(len(board)):
        print(f"{board[i][0]}\t{board[i][1]}\t{board[i][2]}")
        print()

if __name__=='__main__':
    goal_board = [[1,2,3],[4,5,6],[7,8,-1]]
    # board = []
    # for i in range(0,3):
    #     new_arr = []
    #     for j in range(0,3):
    #         new_arr.append(int(input(f"Enter {i}{j}: ")))
    #     board.append(new_arr)
    board = [[1,2,3],[-1,4,6],[7,5,8]]
    already_visited = []
    g_n = 0
    while(check(goal_board,board)==False):
        already_visited.append(board)
        print_board(board)
        g_n+=1
        new_boards = []
        min_val = math.inf
        min_idx = math.inf
        for i in range(4):
            new_board = move(board,i)
            h_n = get_hn(goal_board,new_board)
            f_n = g_n+h_n
            if((f_n<min_val) and (new_board not in already_visited)):
                min_val = f_n
                min_idx = i
            new_boards.append(new_board)
        board = new_boards[min_idx]
    print_board(board)

    