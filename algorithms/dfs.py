from collections import deque
from models.Node import Node 
from models.Direction import Direction
from models.State import State

def dfs(initial_state, map):
    frontier = deque([Node(initial_state)])
    explored = set()

    while frontier:
        node = frontier.pop()

        # Check if we have reached the goal state
        if node.state.is_goal_state(map):
            return node.path()

        explored.add(node.state)

        # Explore neighbors
        for direction in Direction:
            child_state = node.state.move(direction, map)
            if child_state and child_state not in explored:
                frontier.append(Node(child_state, node, direction))
    
    # Return None if no solution is found
    return None
