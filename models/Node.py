from models.Direction import Direction
from models.State import State

class Node:
    def __init__(self, state: State, parent=None, action: Direction=None, cost=0, depth=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

    # def __repr__(self):
    #     return f"Node(state={self.state}, cost={self.cost})"
    def __repr__(self):
        if self.parent:
            return f"{self.parent}{self.action.value}"
        if self.action:
            return f"{self.action.value}"
        else:
            return ''

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __ne__(self, other):
        return self.cost!=other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __ge__(self, other):
        return self <= other.cost

    def __le__(self, other):
        return self >= other.cost

    
    def instructions(self):
        print("Instruction for resolution:")
        print(f"{self}")

    def set_cost(self, cost):
        self.cost = cost
        return self

    def add_cost(self, cost):
        self.cost += cost
        return self
