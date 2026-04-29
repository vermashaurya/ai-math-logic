import os
import json

base_dir = "algorithms"
output_file = "website/src/data/algorithms.json"

algorithms = []

titles = {
    "4-queens": "4-Queens Problem",
    "8-puzzle": "8-Puzzle Solver",
    "bayesian-classification": "Bayesian Classification",
    "crypt-arithmetic": "Crypt-Arithmetic",
    "decision-tree": "Decision Tree",
    "dijkstras-algo": "Dijkstra's Algorithm",
    "mcts": "Monte Carlo Tree Search",
    "missionaries-and-cannibals": "Missionaries & Cannibals",
    "n-queens": "N-Queens Solver",
    "pathfinder-maze": "Pathfinder (Maze)",
    "tsp": "Traveling Salesperson",
    "water-jug": "Water Jug Problem"
}

tags_map = {
    "4-queens": ["Search", "Backtracking"],
    "8-puzzle": ["Search", "Heuristics"],
    "bayesian-classification": ["Machine Learning", "Probability"],
    "crypt-arithmetic": ["Constraint Satisfaction"],
    "decision-tree": ["Machine Learning"],
    "dijkstras-algo": ["Graph", "Pathfinding"],
    "mcts": ["Search", "Game Theory"],
    "missionaries-and-cannibals": ["Search", "Logic"],
    "n-queens": ["Search", "Backtracking"],
    "pathfinder-maze": ["Graph", "Pathfinding"],
    "tsp": ["Optimization", "Graph"],
    "water-jug": ["Search", "Logic"]
}

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        files_data = []
        for file in os.listdir(folder_path):
            if file.endswith('.py'):
                with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                files_data.append({
                    "name": file,
                    "content": content
                })
        
        if files_data:
            algorithms.append({
                "id": folder,
                "title": titles.get(folder, folder.replace("-", " ").title()),
                "tags": tags_map.get(folder, ["Algorithm"]),
                "files": files_data
            })

os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(algorithms, f, indent=2)

print(f"Generated {output_file} with {len(algorithms)} algorithms.")
