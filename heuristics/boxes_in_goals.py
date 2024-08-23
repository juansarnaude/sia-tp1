

def boxes_in_goals(node = None, map = None):
    if map:
        boxes_in_goals.map = map
        boxes_in_goals.n_boxes = len(map.boxes)
        return
    else:
        node.add_cost(  boxes_in_goals.n_boxes / (len(node.state.boxes.intersection(boxes_in_goals.map.goals))+1)  )
        return

