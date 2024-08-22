from collections import deque
from queue import PriorityQueue
from models.Node import Node 
from models.Direction import Direction

def local_greedy(initial_state, map, heuristics):
    inner_frontier = PriorityQueue()
    frontier = deque([Node(initial_state)])
    explored = set()

    while frontier:
        node = frontier.pop()

        # Check if we have reached the goal state
        if node.state.is_goal_state(map):
            return node, len(explored), len(frontier)

        explored.add(node.state)

        # Explore neighbors
        for direction in Direction:
            child_state = node.state.move(direction, map)
            heuristics.apply(node)
            if child_state and child_state not in explored:
                new_node = Node(child_state, node, direction)
                heuristics.apply(new_node)
                inner_frontier.put((new_node.cost, new_node))
        
        #Add elements ordered by cost
        while not inner_frontier.empty():
            _, aux_node = inner_frontier.get()
            frontier.append(aux_node)

    # Return None if no solution is found
    return None, len(explored), len(frontier)
