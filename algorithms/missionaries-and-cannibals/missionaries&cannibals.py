from collections import deque

initial_state = (3, 3, 'L')  
goal_state = (0, 0, 'R')

def is_valid(state):
    num_missionaries_left, num_cannibals_left, boat_position = state

    if num_missionaries_left > 0 and num_cannibals_left > num_missionaries_left:
        return False

    num_missionaries_right = 3 - num_missionaries_left
    num_cannibals_right = 3 - num_cannibals_left

    if num_missionaries_right > 0 and num_cannibals_right > num_missionaries_right:
        return False

    return True

def generate_moves(state):
    moves = []
    num_missionaries_left, num_cannibals_left, boat_position = state

    if boat_position == 'L':
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2 and num_missionaries_left - i >= 0 and num_missionaries_left - i <= 3:
                    new_state = (num_missionaries_left - i, num_cannibals_left - j, 'R')
                    if is_valid(new_state):
                        moves.append((new_state, f"{i} missionaries and {j} cannibals cross left"))

                if i + j > 0 and i + j <= 2 and num_cannibals_left - i >= 0 and num_cannibals_left - i <= 3:
                    new_state = (num_missionaries_left - j, num_cannibals_left - i, 'R')
                    if is_valid(new_state):
                        moves.append((new_state, f"{j} missionaries and {i} cannibals cross left"))
    else:
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2 and num_missionaries_left + i >= 0 and num_missionaries_left + i <= 3:
                    new_state = (num_missionaries_left + i, num_cannibals_left + j, 'L')
                    if is_valid(new_state):
                        moves.append((new_state, f"{i} missionaries and {j} cannibals come back"))

                if i + j > 0 and i + j <= 2 and num_cannibals_left + i >= 0 and num_cannibals_left + i <= 3:
                    new_state = (num_missionaries_left + j, num_cannibals_left + i, 'L')
                    if is_valid(new_state):
                        moves.append((new_state, f"{j} missionaries and {i} cannibals come back"))

    return moves

def solve():
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path

        if state not in visited:
            visited.add(state)
            moves = generate_moves(state)
            for move, phrase in moves:
                queue.append((move, path + [phrase]))

    return None

print("Initial state:")
print(f"Missionaries: {initial_state[0]}, Cannibals: {initial_state[1]}")
print(f"Boat position: {initial_state[2]}")
print()

solution = solve()

if solution is None:
    print("No solution found.")
else:
    print("Solution:")
    for phrase in solution:
        print(phrase)

print()
print("Final state:")
print(f"Missionaries: {goal_state[0]}, Cannibals: {goal_state[1]}")
print(f"Boat position: {goal_state[2]}")
