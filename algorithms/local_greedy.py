from collections import deque
from models.Node import Node
from models.Direction import Direction

def local_greedy(initial_state, map, heuristics):
    frontier = deque([Node(initial_state)])
    explored = set()
    discarded_count = 0
    unexplored_children = []

    while frontier or unexplored_children:
        if not frontier:
            # Backtrack to the most recent unexplored children
            unexplored_children.sort(key=lambda x: x.cost)
            frontier.append(unexplored_children[0])
            unexplored_children.remove(unexplored_children[0])

        node = frontier.pop()

        # Check if we have reached the goal state
        if node.state.is_goal_state(map):
            return node, len(explored), len(frontier) + len(unexplored_children), discarded_count

        explored.add(node.state)

        # List to temporarily hold the children nodes
        children = []

        # Explore neighbors
        for direction in Direction:
            child_state = node.state.move(direction, map)

            if child_state and child_state not in explored:
                new_node = Node(child_state, node, direction)
                heuristics.apply(new_node)
                children.append(new_node)
            elif child_state and child_state in explored:
                discarded_count += 1

        # Sort children by their heuristic cost (ascending order)
        children.sort(key=lambda x: x.cost)

        if children:
            # Add the lowest-cost child to the frontier
            frontier.append(children[0])

            # Store the rest of the children for later exploration
            unexplored_children.extend(children[1:])

    # Return None if no solution is found
    return None, len(explored), len(frontier) + len(unexplored_children), discarded_count
