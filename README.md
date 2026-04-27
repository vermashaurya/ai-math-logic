# AI Math Logic & Fundamentals

![UI Preview](https://img.shields.io/badge/UI-Vite%20React-blue?style=for-the-badge&logo=react)
![Python](https://img.shields.io/badge/Algorithms-Python-yellow?style=for-the-badge&logo=python)

This repository contains classical and challenging problems one faces while learning Artificial Intelligence, Mathematics, and Logic. The algorithms have been refactored and organized into distinct modules, and we have built a **beautiful, interactive web interface** to explore them.

## 🌟 Web User Interface

We have built a premium, glassmorphism-styled React application to browse and explore all the algorithms directly in your browser. 
Once deployed to GitHub Pages, you'll be able to view the problem descriptions, categorize by tags, and read the syntax-highlighted source code!

> **To run the UI locally:**
> ```bash
> cd website
> npm install
> npm run dev
> ```

## 🧩 The Algorithms

The `algorithms/` folder contains Python implementations of various AI and search problems, including:

- **4-Queens & N-Queens Problems**: Backtracking algorithms to place N non-attacking queens on an N×N chessboard.
- **8-Puzzle**: Solving the sliding puzzle using Search & Heuristics (including Hill Climbing).
- **Water Jug Problem**: A classic logic puzzle to measure an exact amount of water using two jugs.
- **Missionaries & Cannibals**: A river-crossing puzzle solved using Logic & Search.
- **Pathfinder (Maze)**: Graph pathfinding in a 2D grid.
- **Traveling Salesperson (TSP)**: Optimization problem solved via BFS and Greedy approaches.
- **Bayesian Classification**: Machine Learning models (Naive Bayes & Random Forest) for spam classification.
- **Decision Trees**: A predictive modeling approach.
- **Monte Carlo Tree Search (MCTS)**: Advanced game theory search algorithm.
- **Crypt-Arithmetic**: Constraint satisfaction problems.
- **Dijkstra's Algorithm**: Finding the shortest paths between nodes in a graph.

Methods used to achieve desirable solutions include **BFS (Breadth-First Search)**, **DFS (Depth-First Search)**, **Backtracking**, and **Heuristics**.

## 📸 Previews

### N-Queens Problem
<center><img width="452" alt="image" src="https://github.com/vermashaurya/ai-foundational/assets/136727534/d881a8c9-43ce-47bc-8d4d-e8a5a4ecffe4"></center>

### Waterjug Problem
<center><img width="452" alt="image" src="https://github.com/vermashaurya/ai-foundational/assets/136727534/7378a387-4fa7-4139-a894-f96fa0e12217"></center>

### Pathfinding in a Maze
<center><img width="452" alt="image" src="https://github.com/vermashaurya/ai-foundational/assets/136727534/dea64d16-bf1e-4c6b-9b0d-2912bd9fdd6f"></center>

### 8 Puzzle Problem
<center><img width="452" alt="image" src="https://github.com/vermashaurya/ai-foundational/assets/136727534/0d4c06b6-eca5-4917-822f-1c98257c31c9"></center>

### Missionary & Cannibals Problem
<center><img width="452" alt="image" src="https://github.com/vermashaurya/ai-foundational/assets/136727534/f8413202-84fa-4758-abe5-f81a4adbc518"></center>

## 📂 Project Structure

```text
.
├── README.md
├── algorithms/
│   ├── 4-queens/
│   ├── 8-puzzle/
│   ├── bayesian-classification/
│   ├── crypt-arithmetic/
│   ├── decision-tree/
│   ├── dijkstras-algo/
│   ├── mcts/
│   ├── missionaries-and-cannibals/
│   ├── n-queens/
│   ├── pathfinder-maze/
│   ├── tsp/
│   └── water-jug/
├── automation/
│   └── instagram-caption-generator/
├── website/                 # React Vite Web UI
└── generate_data.py         # Script to extract python files to UI data
```

## 🤝 Contributing
Feel free to add to this folder or improve the web interface. Happy Coding!
