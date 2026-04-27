import random

class Node:
    def __init__(self, state):
        self.state = state
        self.visits = 0
        self.score = 0
        self.children = []

def simulate(node):
    # Perform a random playout from the given node's state
    # and return the final score
    # Here, we can simulate random moves and calculate the score

    # This is a simplified example, the actual simulation will depend on the game mechanics

    # Simulate random moves until a terminal state is reached
    while not node.state.is_terminal():
        moves = node.state.get_possible_moves()
        random_move = random.choice(moves)
        node.state.make_move(random_move)

    # Calculate and return the final score
    return node.state.calculate_score()

def select(node):
    # Select the child node with the highest UCB (Upper Confidence Bound) score
    # based on the exploration-exploitation trade-off

    # This is a simplified example, the actual selection mechanism will depend on UCB calculation

    selected_node = max(node.children, key=lambda child: child.score / child.visits +
                                                       math.sqrt(2 * math.log(node.visits) / child.visits))
    return selected_node

def expand(node):
    # Expand the given node by adding child nodes for each possible move
    moves = node.state.get_possible_moves()
    for move in moves:
        new_state = node.state.apply_move(move)
        new_node = Node(new_state)
        node.children.append(new_node)

def backpropagate(node, score):
    # Update the visit count and score of the node and its ancestors
    node.visits += 1
    node.score += score
    if node.parent:
        backpropagate(node.parent, score)

def monte_carlo_tree_search(root_node, iterations):
    for _ in range(iterations):
        selected_node = select(root_node)
        expand(selected_node)
        score = simulate(selected_node)
        backpropagate(selected_node, score)

    # Select the best move based on the highest average score
    best_child = max(root_node.children, key=lambda child: child.score / child.visits)
    best_move = best_child.state.last_move
    return best_move
