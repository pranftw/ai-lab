import random

class Agent:
    def _init__(self, player_type, pawn):
        self.player_type=player_type
        self.pawn = pawn
    
    def make_move(self, move, game_arr):
        square = move
        game_arr[int(square)] = self.pawn
    
    def check_move(self, move, game_arr):
        square= move
        if(game_arr[square]!"-"):
            return False
        else:
            return True
    
    def think(self, game_arr, num_moves):
        if(self.player_type=="Computer"):
            best_move = self.find_move(game_arr, num_moves)
            self.make_move(best_move)
        elif(self.player_type=="Human"):
            best_move = int(input("enter the move:"))
            move_correctness = self.check_move(best_move) 
            if(move_correctness):
                self.make_move(best_move)
            else:
                self.think()
    
    def check_if_agent_is_winning(self, game_arr, pawn):
        end_states = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        count = 0
        for end_state in end_states:
            states = []
            if(game_arr[end_state[0]]==pawn):
                count+=1
            else:
                states.append(end_state[0])
            if(game_arr[end_state[1]]==pawn):
                count+=1
            else:
                states.append(end_state[1])
            if(game_arr[end_state[2]]==pawn):
                count+=1
            else:
                states.append(end_state[2])
            
            if(count==2 and game_arr[states[0]]=="-"):
                return [True, states]
            else:
                count = 0
        return [False, states]
    
    def find_move(self, game_arr, num_moves):
        if(num_moves==0):
            move=random.choice([0,2,6,8])
        else:
            opponents_pawn = "x" if(self.pawn=="o") else "o"
            opponent_winning = self.check_if_agent_is_winning(game_arr, opponents_pawn)
            me_winning = self.check_if_agent_is_winning(game_arr, self.pawn)
            if(opponent_winning[0]):
                move = opponent_winning[1]
            elif(me_winning[0]):
                move = me_winning[1]
            else:
                pass

        return move




class Game:
    def __init__(self, player_1_type, player_1_pawn, player_2_type, player_2_pawn):
        self.game_arr = []
        self.moves = 0
        self.end_states = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        for  in range(9):
            self.game_arr.append("-")
        
        self.agent_1 = Agent(player_1_type,player_1_pawn)
        self.agent_2 = Agent(player_2_type,player_2_pawn)

    def play(self):

        while(self.check_if_game_over()[0] is False):
            self.agent_1.think()
            self.moves+=1
            if(self.check_if_game_over()[0] is False):
                self.agent_2.think()
                self.moves+=1
            else:
                print("GAME OVER")
        print("GAME OVER") 

    def show_board(self):
        start = 0
        board_str = "\n"
        while(start<9):
            board_str+="\t".join(self.game_arr[start:start+3])
            board_str+="\n"
            start+=3 
        print(board_str)

    def game_over_tester(self, pawn):
        game_over = False
        for end_state in self.end_states:
            if(self.game_arr[end_state[0]]==pawn and self.game_arr[end_state[1]]==pawn and self.game_arr[end_state[2]]==pawn):
                game_over = True
                break
        return game_over

    def check_if_game_over(self):
        did_x_win = self.game_over_tester("x")
        did_y_win = False

        if(not(did_x_win)):
            did_y_win = self.game_over_tester("o")
        if(did_x_win):
            return [True, "x"]
        elif(did_y_win):
            return [True, "o"]
        elif(self.moves==9):
            return [True, "draw"]
        else:
            return [False, "_"]


if __name__=='__main__':
    game = Game("Computer","x","Human","y")


        

