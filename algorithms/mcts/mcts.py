import random

class Node:
    def __init__(self, state):
        self.state = state
        self.visits = 0
        self.score = 0
        self.children = []

def simulate(node):

    while not node.state.is_terminal():
        moves = node.state.get_possible_moves()
        random_move = random.choice(moves)
        node.state.make_move(random_move)

    return node.state.calculate_score()

def select(node):

    selected_node = max(node.children, key=lambda child: child.score / child.visits +
                                                       math.sqrt(2 * math.log(node.visits) / child.visits))
    return selected_node

def expand(node):
    moves = node.state.get_possible_moves()
    for move in moves:
        new_state = node.state.apply_move(move)
        new_node = Node(new_state)
        node.children.append(new_node)

def backpropagate(node, score):
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

    best_child = max(root_node.children, key=lambda child: child.score / child.visits)
    best_move = best_child.state.last_move
    return best_move
