maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '#', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

start = (1, 1)
end = (5, 9)

num_rows = len(maze)
num_cols = len(maze[0])

def dfs(current, path):
    if current == end:
        return path

    row, col = current
    maze[row][col] = '#'

    neighbors = get_neighbors(current)
    for neighbor in neighbors:
        result = dfs(neighbor, path + [neighbor])
        if result is not None:
            return result

    return None

def get_neighbors(position):
    row, col = position
    neighbors = []

    # Right
    if col + 1 < num_cols and maze[row][col + 1] != '#':
        neighbors.append((row, col + 1))

    # Left
    if col - 1 >= 0 and maze[row][col - 1] != '#':
        neighbors.append((row, col - 1))

    # Down
    if row + 1 < num_rows and maze[row + 1][col] != '#':
        neighbors.append((row + 1, col))

    # Up
    if row - 1 >= 0 and maze[row - 1][col] != '#':
        neighbors.append((row - 1, col))

    return neighbors

path = dfs(start, [start])

if path is not None:
    print("Path found:")
    for position in path:
        print(position)
else:
    print("No path found.")
