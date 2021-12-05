from copy import deepcopy

# This will be a no nonsense tic tac toe implementation without using OOJ

def print_board(board):
    print()
    for i in range(len(board)):
        print(f"{board[i][0]}\t{board[i][1]}\t{board[i][2]}")
        print()
    print()


def game_over(board, num_moves, print_val=False): # Check if someone has won the game or its a draw
    # Return 0 if x won, 1 if y won, 2 if draw, 3 if nothing
    winner = None
    if((board[0][0]==board[0][1]==board[0][2]) and (board[0][0]!=None)):
        winner = board[0][0]
    elif((board[0][0]==board[1][0]==board[2][0]) and (board[0][0]!=None)):
        winner = board[0][0]
    elif((board[0][0]==board[1][1]==board[2][2]) and (board[0][0]!=None)):
        winner = board[0][0]
    elif((board[0][2]==board[1][2]==board[2][2]) and (board[0][2]!=None)):
        winner = board[0][2]
    elif((board[2][0]==board[2][1]==board[2][2]) and (board[2][0]!=None)):
        winner = board[2][0]
    elif((board[0][2]==board[1][1]==board[2][0]) and (board[0][2]!=None)):
        winner = board[0][2]
    elif((board[0][1]==board[1][1]==board[2][1]) and (board[0][1]!=None)):
        winner = board[0][1]
    elif((board[1][0]==board[1][1]==board[1][2]) and (board[1][0]!=None)):
        winner = board[1][0]

    if(winner is None and num_moves==9):
        if(print_val):
            print("\nIt is a draw!")
        return 2
    if(winner=="x"):
        if(print_val):
            print("\nx wins!")
        return 0
    elif(winner=="o"):
        if(print_val):
            print("\no wins!")
        return 1
    return 3

def check_move(board, x, y): # Move can only be allowed if the value in that index is None
    in_range = (x in range(3)) and (y in range(3))
    if(in_range):
        element_present = True if(board[x][y]) else False
        if(element_present):
            return False
        return True
    return False

def all_board_possibilities(board, pawn, num_moves):
    # Check for all possibilities on the board if all None in the board are replaced by "pawn" in the board everytime
    # and everytime a new board appears, giving all possibilities.
    # If x is pawn and x is winning, then that move will be returned, so on that move o(computer)
    # can play o in that coordinates and hence prevent it from winning. Same appears if pawn is o
    possibilities = []
    moves = []
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==None):
                board_x = deepcopy(board)
                board_x[i][j] = pawn
                possibilities.append(board_x)
                moves.append((i,j))
    for i,p in enumerate(possibilities):
        go = game_over(p,num_moves)
        if((pawn=="x" and go==0) or (pawn=="o" and go==1)):
            return moves[i]
    return None

def make_consecutives(board, computer_pawn):
    # If no one, x or o is winning, then try to make consecutive pawns be it left,right,up,down or diagonals.
    """
        Example:
            before 
                o - -
                x - -
                - - -
            
            after
                o o -
                x - -
                - - -

                or

                o - -
                x o -
                - - -
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==computer_pawn):
                if(i-1>=0 and board[i-1][j]==None):
                    return (i-1,j)
                if(i+1<len(board) and board[i+1][j]==None):
                    return (i+1,j)
                if(j-1>=0 and board[i][j-1]==None):
                    return (i,j-1)
                if(j+1<len(board) and board[i][j+1]==None):
                    return (i,j+1)
                if((i-1>=0 and j-1>=0) and board[i-1][j-1]==None):
                    return (i-1,j-1)
                if((i-1>=0 and j+1<len(board)) and board[i-1][j+1]==None):
                    return (i-1,j+1)
                if((i+1<len(board) and j-1>=0) and board[i+1][j-1]==None):
                    return (i+1,j-1)
                if((i+1<len(board) and j+1<len(board)) and board[i+1][j+1]==None):
                    return (i+1,j+1)
    return None

def search_move(board, computer_pawn, user_pawn, num_moves): # Computer to search for an optimal move
    does_user_win = all_board_possibilities(board,user_pawn,num_moves)
    if(does_user_win!=None):
        return make_move(board,does_user_win[0],does_user_win[1],computer_pawn)
    does_computer_win = all_board_possibilities(board,computer_pawn,num_moves)
    if(does_computer_win!=None):
        return make_move(board,does_computer_win[0],does_computer_win[1],computer_pawn)
    consecutives = make_consecutives(board,computer_pawn)
    if(consecutives!=None):
        return make_move(board,consecutives[0],consecutives[1],computer_pawn)
    # if none of them win and consecutives also aren't possible, then make the move anywhere it is None  
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==None):
                return make_move(board,i,j,computer_pawn)

def get_move(board): # Get the move from the user FORMAT-> x y, where they are indices of the board
    while(True):
        move_str = input("Enter the move: ")
        move_str_split = move_str.split(" ")
        try:
            x = int(move_str_split[0])
            y = int(move_str_split[1])
        except:
            print("Invalid move format! Try again.\n")
            continue
        if(check_move(board,x,y)):
            return x,y
        print("Invalid move! Try again.\n")

def choose_pawn():
    while(True):
        user_pawn = input("Choose x or o: ")
        if(user_pawn=="x"):
            computer_pawn = "o"
            break
        if(user_pawn=="o"):
            computer_pawn = "x"
            break
        print("Invalid input! Try again!\n")
    return user_pawn, computer_pawn

def make_move(board, x, y, player): # Make the move on the board
    board = deepcopy(board)
    board[x][y] = player
    return board

def play(board): # Main function which is the communication bw the board and user
    # Allow the user to chose if he needs x or o
    user_pawn, computer_pawn = choose_pawn()
    num_moves = 0
    if(computer_pawn=="x"):
        players = [computer_pawn, user_pawn]
    else:
        players = [user_pawn, computer_pawn]
    while(game_over(board,num_moves,True)==3):
        print_board(board)
        curr_player = players[num_moves%len(players)]
        if(curr_player==computer_pawn):
            board = search_move(board, computer_pawn, user_pawn, num_moves)
        else:
            x,y = get_move(board)
            board = make_move(board,x,y,curr_player)
        num_moves+=1
    return board

if __name__=='__main__':
    board = [[],[],[]]
    for row in range(len(board)): # Create empty board and initialize everything with None
        for _ in range(len(board)):
            board[row].append(None)
    board = play(board)


