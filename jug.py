def push(s,new_state): # new_state - (jug1, jug2)
    s.append(new_state)

def pop(s):
    return s.pop(0)

def fill(jug, jug_capacity):
    return jug_capacity

def discard(jug):
    return 0

def pour(jug1,jug2,jug1_capacity,jug2_capacity):
    jug2 = jug2 + jug1
    if(jug2>jug2_capacity):
        jug1 = jug2 - jug2_capacity
    return (jug1, jug2)

def get_all_possibilities(jug1, jug2, jug1_capacity, jug2_capacity):
    possibilities = []
    jug1_temp = jug1
    jug2_temp = jug2
    jug1 = jug1_temp
    jug2 = jug2_temp
    jug1 = fill(jug1, jug1_capacity)
    possibilities.append((jug1,jug2))
    jug1 = jug1_temp
    jug2 = jug2_temp
    jug2 = fill(jug2, jug2_capacity)
    possibilities.append((jug1,jug2))
    jug1 = jug1_temp
    jug2 = jug2_temp
    jug1 = discard(jug1)
    possibilities.append((jug1,jug2))
    jug1 = jug1_temp
    jug2 = jug2_temp
    jug2 = discard(jug2)
    possibilities.append((jug1,jug2))
    jug1 = jug1_temp
    jug2 = jug2_temp
    jug1,jug2 = pour(jug1,jug2,jug1_capacity,jug2_capacity)
    possibilities.append((jug1,jug2))
    jug1 = jug1_temp
    jug2 = jug2_temp
    jug2,jug1 = pour(jug2,jug1,jug2_capacity,jug1_capacity)
    possibilities.append((jug1,jug2))
    return possibilities

def check(jug1, jug2, goal_capacity):
    return (jug1==goal_capacity or jug2==goal_capacity)

def solve(s, jug1_capacity, jug2_capacity, goal_capacity):
    jug1 = 0
    jug2 = 0
    visited = []
    push(s,(jug1,jug2))
    while(len(s)!=0):
        jug1,jug2 = pop(s)
        if(check(jug1,jug2,goal_capacity)):
            print(f"Solved! {jug1} {jug2}")
            return
        possibilities = get_all_possibilities(jug1, jug2, jug1_capacity, jug2_capacity)
        for p in possibilities:
            if(p not in visited):
                push(s,p)
    print("Unsolvable!")

if __name__=='__main__':
    jug1_capacity = int(input("Enter the capacity of jug1: "))
    jug2_capacity = int(input("Enter the capacity of jug2: "))
    goal_capacity = int(input("Enter the goal capacity: "))
    s = []
    solve(s,jug1_capacity,jug2_capacity,goal_capacity)
