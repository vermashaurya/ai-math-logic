from collections import deque

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def tsp_bfs(cities):
    num_cities = len(cities)

    queue = deque([(i, set([i])) for i in range(1, num_cities)])

    min_cost = float('inf')
    optimal_path = None

    while queue:
        city, visited = queue.popleft()

        if len(visited) == num_cities:
            visited.add(0)

            cost = 0
            path = [cities[i] for i in visited]
            for i in range(num_cities):
                cost += distance(path[i], path[(i + 1) % num_cities])

            if cost < min_cost:
                min_cost = cost
                optimal_path = list(visited)

        else:
            for next_city in range(num_cities):
                if next_city not in visited:
                    new_visited = visited.copy()
                    new_visited.add(next_city)
                    queue.append((next_city, new_visited))

    return min_cost, optimal_path

cities = [(0, 0), (1, 2), (3, 1), (2, 3), (4, 4)]
optimal_cost, optimal_path = tsp_bfs(cities)

if optimal_path is not None:
    print("Optimal Path:")
    for city_index in optimal_path:
        print(cities[city_index])
    print("Optimal Cost:", optimal_cost)
else:
    print("No solution found.")
