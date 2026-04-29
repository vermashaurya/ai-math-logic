initial_state = [
    [1, 0, 2],
    [4, 5, 3],
    [7, 8, 6]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
action_labels = ['Left', 'Right', 'Up', 'Down']

def dfs(current_state, path, visited):
    if current_state == goal_state:
        return path

    visited.add(tuple(map(tuple, current_state)))  

    row, col = find_empty_tile(current_state)

    for action, label in zip(actions, action_labels):
        new_row = row + action[0]
        new_col = col + action[1]

        if is_valid_move(new_row, new_col):
            new_state = create_new_state(current_state, row, col, new_row, new_col)

            if tuple(map(tuple, new_state)) not in visited:
                result = dfs(new_state, path + [label], visited)

                if result is not None:
                    return result

    return None

def find_empty_tile(state):
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 0:
                return row, col

def is_valid_move(row, col):
    return 0 <= row < 3 and 0 <= col < 3

def create_new_state(state, row, col, new_row, new_col):
    new_state = [row[:] for row in state]
    new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
    return new_state

print("Initial State:")
for row in initial_state:
    print(row)
print()

print("Goal State:")
for row in goal_state:
    print(row)
print()

path = dfs(initial_state, [], set())

if path is not None:
    print("Path found:")
    for step, action in enumerate(path, start=1):
        print(f"Step {step}: {action}")
else:
    print("No solution found.")
