import random

initial_state = [
    [4, 1, 2],
    [7, 3, 0],
    [8, 5, 6]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
action_labels = ['Up', 'Down', 'Left', 'Right']

def heuristic(state):
    misplaced = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced

def hill_climbing(initial_state, goal_state, max_restarts=1000):
    actions_taken = []
    restarts = 0

    while restarts < max_restarts:
        current_state = initial_state
        current_cost = heuristic(current_state)

        for _ in range(max_restarts):
            if current_state == goal_state:
                return actions_taken

            neighbors = []

            row, col = find_empty_tile(current_state)

            for action, label in zip(actions, action_labels):
                new_row = row + action[0]
                new_col = col + action[1]

                if is_valid_move(new_row, new_col):
                    new_state = create_new_state(current_state, row, col, new_row, new_col)
                    neighbors.append((new_state, label))

            best_neighbor = None
            best_cost = float('inf')

            for neighbor, label in neighbors:
                neighbor_cost = heuristic(neighbor)
                if neighbor_cost < best_cost:
                    best_neighbor = neighbor
                    best_cost = neighbor_cost
                    best_label = label

            if best_neighbor is None:
                break

            actions_taken.append(best_label)

            current_state = best_neighbor
            current_cost = best_cost

        restarts += 1

    return []

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

actions = hill_climbing(initial_state, goal_state)

if actions:
    print("Actions taken:")
    for action in actions:
        print(action)
else:
    print("No solution found.")
