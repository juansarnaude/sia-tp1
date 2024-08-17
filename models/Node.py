from models.Direction import Direction

class Node:
    def __init__(self, state, parent=None, action: Direction=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    # def __repr__(self):
    #     return f"Node(state={self.state}, cost={self.cost})"
    def __repr__(self):
        if self.parent:
            return f"{self.parent} {self.action.value}"
        return f"{self.action}"
    
    def instructions(self):
        print("Instruction for resolution:")
        print(f"{self}")
