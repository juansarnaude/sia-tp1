class State:
    def __init__(self, player, boxes):
        self.player = player
        self.boxes = frozenset(boxes)

    def __eq__(self, other):
        return self.player == other.player and self.boxes == other.boxes

    def __hash__(self):
        return hash((self.player, self.boxes))

    def move(self, direction, game_map):
        new_player = self.player.move(direction)
        if game_map.is_wall(new_player):
            return None
        
        new_boxes = set(self.boxes)
        if new_player in new_boxes:
            new_box_pos = new_player.move(direction)
            if game_map.is_wall(new_box_pos) or new_box_pos in new_boxes:
                return None
            new_boxes.remove(new_player)
            new_boxes.add(new_box_pos)
        
        return State(new_player, new_boxes)

    def is_goal_state(self, game_map):
        return all(box in game_map.goals for box in self.boxes)

    def __repr__(self):
        return f"State(player={self.player}, boxes={self.boxes})"
