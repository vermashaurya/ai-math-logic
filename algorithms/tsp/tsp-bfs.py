from collections import deque

# Function to calculate the distance between two cities
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Function to solve the Traveling Salesman Problem using BFS
def tsp_bfs(cities):
    num_cities = len(cities)

    # Create a queue to store the states (city, visited) for BFS traversal
    queue = deque([(i, set([i])) for i in range(1, num_cities)])

    # Initialize the minimum cost and optimal path
    min_cost = float('inf')
    optimal_path = None

    while queue:
        city, visited = queue.popleft()

        # Check if all cities have been visited
        if len(visited) == num_cities:
            # Add the starting city to complete the cycle
            visited.add(0)

            # Calculate the cost of the current path
            cost = 0
            path = [cities[i] for i in visited]
            for i in range(num_cities):
                cost += distance(path[i], path[(i + 1) % num_cities])

            # Update the minimum cost and optimal path if necessary
            if cost < min_cost:
                min_cost = cost
                optimal_path = list(visited)

        else:
            # Generate the next possible cities to visit
            for next_city in range(num_cities):
                if next_city not in visited:
                    new_visited = visited.copy()
                    new_visited.add(next_city)
                    queue.append((next_city, new_visited))

    # Return the optimal cost and path
    return min_cost, optimal_path

# Test the algorithm
cities = [(0, 0), (1, 2), (3, 1), (2, 3), (4, 4)]
optimal_cost, optimal_path = tsp_bfs(cities)

if optimal_path is not None:
    print("Optimal Path:")
    for city_index in optimal_path:
        print(cities[city_index])
    print("Optimal Cost:", optimal_cost)
else:
    print("No solution found.")
