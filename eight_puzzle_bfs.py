from copy import deepcopy

def pop(q):
    return q.pop(0)

def push(q, new_board_state):
    q.append(new_board_state)

def get_board(): # Get board from the user
    board = []
    for i in range(3):
        for j in range(3):
            while(True):
                try:
                    val = int(input(f"Enter [{i}][{j}]: "))
                    if(val in range(1,9) or val==-1):
                        break
                except:
                    pass
                print("Invalid input! Try again!")
    return board

def validate_board(board): # Validate the board, so that there are no duplicates by summing them all up
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

def print_board(board):
    print()
    for i in range(len(board)):
        print(f"{board[i][0]}\t{board[i][1]}\t{board[i][2]}\t")
    print()

def check(goal_board,board):
    return goal_board==board

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

def solve(goal_board, q):
    while(len(q)!=0):
        board = pop(q)
        print_board(board)
        possibilities = get_all_possibilities(board)
        for p in possibilities:
            if(check(goal_board,p)):
                print("Solved!")
                print_board(p)
                return
            else:
                push(q,p)

if __name__=='__main__':
    goal_board = [[1,2,3],[4,5,6],[7,8,-1]]
    # board = get_board()
    board = [[1,2,3],[-1,4,6],[7,5,8]]
    if(not(validate_board(board))):
        print("Invalid board!")
        exit()
    q = []
    push(q,board)
    solve(goal_board, q)
    