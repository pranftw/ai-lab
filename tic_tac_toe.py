"""
    for diagonals and the middle cross check if the sum is 15 and check if the indices are continuous

    2d representation
    -[0] -[1] -[2]
    -[3] -[4] -[5]
    -[6] -[7] -[8]

    1d representation
    [-[1], -[2], -[3], -[4], -[5], -[6], -[7], -[8], -[9]]
"""

class Agent:
	def __init__(self, player_type, pawn):
		self.player_type = player_type # Human or Computer
		self.pawn = pawn # whether x or o
	
	def make_move(self, move, game_arr):
		square, pawn = move.split(" ")
		game_arr[int(square)] = pawn
	
	def check_move(self, move, game_arr):
		square = int(move.split(" ")[0]) # returns a bool as to whether the move is valid or not
		if(game_arr[square]!="-"):
			return False
		else:
			return True

	def think(self):
		if(self.player_type=="Computer"):
			best_move = self.find_move()
			self.make_move(best_move)
		elif(self.player_type=="Human"):
			best_move = input("Enter the move: ") # which square, x or o
			move_correctness = self.check_move(best_move)
			if(move_correctness):
				self.make_move(best_move)
			else:
				self.think()
	
	def find_move(self, game_arr):
        #first check if you can win or else make sure that the opponent doesn't win
		pass


class Game:
	def __init__(self, player_1_type, player_1_pawn, player_2_type, player_2_pawn):
		self.game_arr = []
		self.moves = 0
        self.end_states = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
		for _ in range(9):
			self.game_arr.append("-")
		agent_1 = Agent(player_1_type,player_1_pawn)
		agent_2 = Agent(player_2_type,player_2_pawn)
	
	def play(self):
		while(self.check_if_game_over() is False):
			agent_1.think()
			self.moves+=1
			if(self.check_if_game_over() is False):
				agent_2.think()
				self.moves+=1
			else:
				print("GAME OVER!")
		print("GAME OVER!")

	def show_board(self):
		start = 0
		board_str = "\n"
		while(start<9):
			board_str+="\t".join(self.game_arr[start:start+3])
			board_str+="\n"
			start+=3
		print(board_str)
    
    def game_over_tester(self, pawn):
        #which is the most efficient way 1) specify all the goal states by hardcoding them 2) try to find a more genius approach to this
        game_over = False
        for end_state in end_states:
            if(self.game_arr[end_state[0]]==pawn and self.game_arr[end_state[1]]==pawn and self.game_arr[end_state[2]]==pawn):
                game_over = True
                break
        return game_over

	def check_if_game_over(self):
        did_x_win = self.game_over_tester("x")
        did_y_win = False
        if(not(did_x_win)):
            did_y_win = self.game_over_tester("y")
        
        if(did_x_win):
            return True, "x"
        elif(did_y_win):
            return True, "y"
        elif(self.moves==9):
            return True, "draw"
        else:
            return False

	 #Check for win or lose or draw and also return who won
    

if __name__=='__main__':
    game = Game("Computer","x","Human","y")