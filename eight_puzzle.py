class Queue:
    def __init__(self):
        self.q = []
    def pop(self):
        self.q.pop(0)
    def push(self, val):
        self.q.append(val)

class Game:
    def __init__(self):
        game_arr_inp = list(int(x) for x in input("Enter the game array: ").split(" "))
        val_game_inp = Game.validate_game_input(game_arr_inp)
        if(not(val_game_inp)):
            print("Invalid game array!")
            exit()
        self.game_arr = []
        self.goal_state = [[1,2,3],[4,5,6],[7,8,-1]]
        self.computed = {}
        self.q = Queue()
        self.moves = []
        start = 0
        while(start<len(game_arr_inp)):
            self.game_arr.append(game_arr_inp[start:start+3])
            start+=3
    
    def check_if_game_over(self, board_state):
        return True if(board_state==self.goal_state) else False
    
    @staticmethod
    def find_empty(board_state):
        for row_num,row in enumerate(board_state):
            for col_num,element in enumerate(row):
                if(element==-1):
                    return [row_num, col_num]

    # direction is 0: left, 1: up, 2: down, 3: right

    @staticmethod
    def validate_direction(empty_idx, direction):
        if(direction==0):
            return True if(empty_idx[1]-1>0) else False
        elif(direction==1):
            return True if(empty_idx[0]-1>0) else False
        elif(direction==2):
            return True if(empty_idx[0]+1>0) else False
        else:
            return True if(empty_idx[1]+1>0) else False
    
    @staticmethod
    def get_board_state_on_move(board_state, empty_idx, direction):
        if(direction==0):
            temp = board_state[empty_idx[0]][empty_idx[1]-1]
            board_state[empty_idx[0]][empty_idx[1]-1] = -1
        elif(direction==1):
            temp = board_state[empty_idx[0]-1][empty_idx[1]]
            board_state[empty_idx[0]-1][empty_idx[1]] = -1
        elif(direction==2):
            temp = board_state[empty_idx[0]+1][empty_idx[1]]
            board_state[empty_idx[0]+1][empty_idx[1]] = -1
        else:
            temp = board_state[empty_idx[0]][empty_idx[1]+1]
            board_state[empty_idx[0]][empty_idx[1]+1] = -1
        board_state[empty_idx[0]][empty_idx[1]] = temp
        return board_state
                

    def bfs(self, board_state):
        Game.print_board_state(board_state)
        if(not(self.check_if_game_over(board_state))):
            empty_idx = Game.find_empty(board_state)
            for i in range(0,4):
                if(Game.validate_direction(empty_idx,i)):
                    self.moves.append(i)
                    new_board_state = Game.get_board_state_on_move(board_state, empty_idx, i)
                    self.bfs(new_board_state)


    @staticmethod
    def validate_game_input(game_arr_inp):
        if(len(game_arr_inp)!=9):
            return False
        elif(len(set(game_arr_inp))!=len(game_arr_inp)):
            return False
        else:
            for inp in game_arr_inp:
                if(not((inp in range(1,9)) or (inp==-1))):
                    return False
        return True
    
    @staticmethod
    def print_board_state(board_state):
        print()
        for i in range(len(board_state)):
            for j in range(len(board_state[i])):
                print(f"{board_state[i][j]}\t",end="")
            print()
        print()
            

if(__name__=='__main__'):
    game = Game()
    game.bfs(game.game_arr)
    print(game.moves)
