from copy import deepcopy
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
	board = deepcopy(board)
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
	print()
	print()
		

def sort_by_fn(fn_vals, new_boards):
	fn_vals = deepcopy(fn_vals)
	new_boards = deepcopy(new_boards)
	while(True):
		swaps = 0
		for i in range(1,len(fn_vals)):
			if(fn_vals[i]<fn_vals[i-1]):
				temp = fn_vals[i]
				fn_vals[i] = fn_vals[i-1]
				fn_vals[i-1] = temp
				temp_board = new_boards[i]
				new_boards[i] = new_boards[i-1]
				new_boards[i-1] = temp_board
				swaps+=1
		if(swaps==0):
			break
	return fn_vals,new_boards

def solve(goal_board, board):
	already_visited = []
	g_n = 0
	while(check(goal_board,board)==False):
		already_visited.append(board)
		print_board(board)
		g_n+=1
		new_boards = []
		fn_vals = []
		for i in range(4):
			new_board = move(board,i)
			h_n = get_hn(goal_board,new_board)
			f_n = g_n+h_n
			fn_vals.append(f_n)
			new_boards.append(new_board)
		fn_vals,new_boards = sort_by_fn(fn_vals,new_boards);
		for b in new_boards:
			if(b not in already_visited):
				board = b
				break
	print_board(board)


if __name__=='__main__':
	goal_board = [[1,2,3],[4,5,6],[7,8,-1]]
	# board = []
	# for i in range(0,3):
	#     new_arr = []
	#     for j in range(0,3):
	#         new_arr.append(int(input(f"Enter {i}{j}: ")))
	#     board.append(new_arr)
	# board = [[1,2,3],[-1,4,6],[7,5,8]]
	board = [[-1,1,3],[4,2,5],[7,8,6]]
	solve(goal_board,board)

    
