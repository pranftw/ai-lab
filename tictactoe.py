from copy import deepcopy

# This will be a no nonsense tic tac toe implementation without using OOJ

def game_over(board, num_moves): # Check if someone has won the game or its a draw
    # Return 0 if x won, 1 if y won, 2 if draw, 3 if nothing
    winner = None
    if((board[0][0]==board[0][1]==board[0][2]) and (board[0][0] is not None)):
        winner = board[0][0]
    elif((board[0][0]==board[1][0]==board[2][0]) and (board[0][0] is not None)):
        winner = board[0][0]
    elif((board[0][0]==board[1][1]==board[2][2]) and (board[0][0] is not None)):
        winner = board[0][0]
    elif((board[0][2]==board[1][2]==board[2][2]) and (board[0][2] is not None)):
        winner = board[0][2]
    elif((board[2][0]==board[2][1]==board[2][2]) and (board[2][0] is not None)):
        winner = board[2][0]
    elif((board[0][2]==board[1][1]==board[2][0]) and (board[0][2] is not None)):
        winner = board[0][2]
    elif((board[0][1]==board[1][1]==board[2][1]) and (board[0][1] is not None)):
        winner = board[0][1]
    elif((board[1][0]==board[1][1]==board[1][2]) and (board[1][0] is not None)):
        winner = board[0][2]

    if(winner is None and num_moves==9):
        print("It is a draw!")
        return 2
    if(winner=="x"):
        print("x wins!")
        return 0
    else:
        print("y wins!")
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

def search_move(board, computer_pawn, num_moves): # Computer to search for an optimal move
    pass

def get_move(board): # Get the move from the user FORMAT-> x y, where they are indices of the board
    while(True):
        move_str = input("Enter the move: ")
        move_str_split = move_str.split(" ")
        try:
            x = int(move_str_split[0])
            y = int(move_str_split[1])
        except:
            print("Invalid move format! Try again.")
            continue
        if(check_move(board,x,y)):
            return x,y
        print("Invalid move! Try again.")

def choose_pawn():
    while(True):
        user_pawn = input("Choose x or o: ")
        if(user_pawn=="x"):
            computer_pawn = "o"
            break
        if(user_pawn=="o"):
            computer_pawn = "x"
            break
        print("Invalid input! Try again!")
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
    while(game_over(board,num_moves)==3):
        curr_player = players[num_moves%len(players)]
        if(curr_player==computer_pawn):
            x,y = search_move(board, computer_pawn, num_moves)
        else:
            x,y = get_move(board)
        board = make_move(board,x,y,curr_player)
        num_moves+=1

if __name__=='__main__':
    board = [[],[],[]]
    for row in range(len(board)): # Create empty board and initialize everything with None
        for _ in range(len(board)):
            board[row].append(None)
    play(board)


