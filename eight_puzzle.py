class Game:
    def __init__(self):
        game_arr_inp = list(int x for x in input("Enter the game array: ").split(" "))
        val_game_inp = validate_game_input(game_arr_inp)
        if(not(val_game_inp)):
            print("Invalid game array!")
            exit()
        self.game_arr = []
        self.goal_state = [[1,2,3],[4,5,6],[7,8,9]]
        self.computed = {}
        start = 0
        while(start<=len(game_arr_inp)):
            self.game_arr.append(game_arr_inp[start:start+3])
            start+=3
    
    def check_if_game_over(self, board_state):
        return True if(board_state==self.goal_state) else False
    
    @staticmethod
    def find_empty(board_state):
        for row_num,row in enumerate(board_state):
            for col_num,element in enumerate(row):
                if(element=="-"):
                    return [row_num, col_num]

    # direction is 0: left, 1: up, 2: down, 3: right

    @staticmethod
    def get_move(board_state, direction):
        empty_idx = find_empty(board_state)
        pass
    
    @staticmethod
    def get_board_state_on_move(move):
        pass

    def recurse(self, board_state):
        if(str(board_state) in self.computed.keys()):
            return self.computed[str(board_state)]
        if(self.check_if_game_over(board_state)):
            return True
        else:
            pass

    @staticmethod
    def validate_game_input(game_arr_inp):
        for inp in game_arr_inp:
            if(not((inp in range(1:9)) or (inp=="-"))):
                return False
        return True
            


