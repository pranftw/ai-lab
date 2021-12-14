def solve(world):
	rows = len(world)
	cols = len(world[0])
	for r in range(rows):
		for c in range(cols):
			agent_location = (r,c)
			if(world[r][c]==1):
				world[r][c] = 0
				print("Suck")
			print_world(world,agent_location)

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
	return world

if __name__=='__main__':
	#world = get_world()
	world = [[1,0,0],[0,1,0],[0,0,0]]
	solve(world)
