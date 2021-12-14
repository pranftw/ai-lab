from copy import deepcopy

def push(q, new_location):
	q.append(new_location)

def pop(q):
	return q.pop(0)

def check(world):
	rows = len(world)
	cols = len(world[0])
	for r in range(rows):
		for c in range(cols):
			if(world[r][c]==1):
				return False
	return True

def take_action(world, agent_location): # If there is dirt, it cleans it up
	if world[agent_location[0]][agent_location[1]]==1:
		world = deepcopy(world)
		world[agent_location[0]][agent_location[1]] = 0
	return world

def get_new_location(world, direction, agent_location): # Gives the new location of the agent DIRECTION -> 0-left, 1-right, 2-up, 3-down
	rows = len(world)
	cols = len(world[0])
	if(direction==0 and (agent_location[0]-1>=0)):
		return (agent_location[0]-1,agent_location[1])
	elif(direction==1 and (agent_location[0]+1<cols)):
		return (agent_location[0]+1,agent_location[1])
	elif(direction==2 and (agent_location[1]-1>=0)):
		return (agent_location[0],agent_location[1]-1)
	elif(direction==3 and (agent_location[1]+1<rows)):
		return (agent_location[0],agent_location[1]+1)
	return None

def get_all_possibilities(world, agent_location): # Get all the possible moves from a square
	possibilities = []
	for i in range(0,4):
		new_location = get_new_location(world,i,agent_location)
		if new_location is not None:
			possibilities.append(((new_location),i)) # i specifies which direction we took
	return possibilities

def solve(world, agent_location, q):
	visited = []
	directions = ["Left","Right","Up","Down"]
	while(len(q)!=0):
		print_world(world,agent_location[0])
		agent_location = pop(q)
		visited.append(agent_location[0])
		print(directions[agent_location[1]])
		world = take_action(world,agent_location[0])
		if(check(world)==True):
			print("Solved!")
			print_world(world,agent_location[0])
			return
		possibilities = get_all_possibilities(world,agent_location[0])
		for p in possibilities:
			if p[0] not in visited:
				push(q,p)
	print("Unsolved!")

def print_world(world, agent_location): # Print the world
	rows = len(world)
	cols = len(world[0])
	print()
	for r in range(rows):
		for c in range(cols):
			if (r,c)==agent_location:
				print_val = "A"
			else:
				print_val = str(world[r][c])
			print(print_val,end="\t")
		print()
	print()

def get_world(): # Take world input from the user
	rows = int(input("Enter the number of rows: "))
	cols = int(input("Enter the number of columns: "))
	world = []
	for r in range(rows):
		new_row = []
		for c in range(cols):
			while True:
				type_cell = int(input(f"\nEnter the status of [{r}][{c}]: "))
				if type_cell not in [0,1]:
					print("Invalid input! Try again!")
				break
			new_row.append(type_cell)
		world.append(new_row)
	while True:
		initial_state_x = int(input("Enter the initial x coordinate of the agent: "))
		initial_state_y = int(input("Enter the initial y coordinate of the agent: "))
		if(initial_state_x in range(0,cols) and initial_state_y in range(0,rows)):
			break
		print("\nInvalid coordinates! Try again!")
	return world, (initial_state_x, initial_state_y)

if __name__=='__main__':
	#world, agent_location = get_world()
	q = []
	world = [[1,0,0],[0,1,0],[0,0,0]]
	agent_location = ((2,2),1)
	push(q,agent_location)
	solve(world, agent_location, q)
