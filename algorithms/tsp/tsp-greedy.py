import math

def distance(city1, city2):
    # Calculate the distance between two cities
    # Replace this with your actual distance calculation method
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def tsp_a_star(cities):
    start_city = cities[0]
    remaining_cities = set(cities[1:])
    visited_cities = frozenset([start_city])
    path = [start_city]
    cost = 0

    while remaining_cities:
        min_cost = math.inf
        min_city = None

        for city in remaining_cities:
            new_cost = cost + distance(path[-1], city)
            if new_cost < min_cost:
                min_cost = new_cost
                min_city = city

        cost = min_cost
        remaining_cities.remove(min_city)
        visited_cities = visited_cities.union([min_city])
        path.append(min_city)

    cost += distance(path[-1], start_city)
    path.append(start_city)

    return cost, path

# Test input
cities = [(0, 0), (1, 2), (3, 4), (1, 1), (2, 2), (4, 3)]

# Run TSP A* algorithm
optimal_cost, optimal_path = tsp_a_star(cities)

print("Optimal Cost:", optimal_cost)
print("Optimal Path:", optimal_path)
