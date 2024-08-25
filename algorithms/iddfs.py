from collections import deque
from models.Node import Node 
from models.Direction import Direction
import math


def iddfs(initial_state, map,iddfs_limit):
    index = 0
    frontier = []
    initial_node = Node(initial_state, cost=0)
    frontier.append(deque([initial_node]))
    frontier.append(deque())
    explored = set()

    while frontier[index]:
        node = frontier[index].pop()

        # Check if we have reached the goal state
        if node.state.is_goal_state(map):
        #    for i in range(index):
        #        print(len(frontier[i]))
           return node,len(explored),len(frontier[index])

        explored.add(node.state)

        # Explore neighbors
        for direction in Direction:
            child_state = node.state.move(direction, map)
            if child_state and child_state not in explored:
                new_node = Node(child_state, node, direction)
                new_node.set_cost(node.cost+1)
                frontier[math.ceil(new_node.cost/iddfs_limit)].append(new_node)

        if not frontier[index]:
            index+=1
            frontier.append(deque())
        
    
    index-=1
    # Return None if no solution is found
    return None, len(explored), len(frontier)

