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
		pass


class Game:
	def __init__(self, player_1_type, player_1_pawn, player_2_type, player_2_pawn):
		self.game_arr = []
		self.moves = 0
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
		board_str = ""
		while(start<9):
			board_str+="\t".join(self.game_arr[start:start+3])
			board_str+="\n"
			start+=3
		print(board_str)

	def check_if_game_over(self):
		pass #Check for win or lose or draw and also return who won