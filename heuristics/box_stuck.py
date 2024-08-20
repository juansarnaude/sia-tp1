from models.Coordinates import Coordinates
from models.Map import Map


def box_stuck(node = None, map = None):
    if not hasattr(box_stuck, "map"):
        box_stuck.map = MapWithMarkedStuckPoints(map)
        return
    else:
        if box_stuck.map.check_stuck_boxes(node.state.boxes):
            node.add_cost(999999)
        return


# MapWithMarkedStuckPoints is an extension of the map class, the only difference
# they have is just that this class has marked the stuck points in which if a box lands there
# the level is unsolvable
class MapWithMarkedStuckPoints(Map):
    def __init__(self, map):
        self.grid = map.grid
        self.goals = map.goals
        self.stuck_points = set()

        self.limit_corners()

    def limit_corners(self):
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                if not self.is_wall(Coordinates(x,y)):
                    if self.is_corner(x, y) and not self.is_goal(Coordinates(x, y)):
                        self.stuck_points.add(Coordinates(x, y))

    def is_corner(self, x, y):
        try:
            left_side = self.is_wall(Coordinates(x-1,y))
            right_side = self.is_wall(Coordinates(x+1,y))
            top_side = self.is_wall(Coordinates(x,y-1))
            bottom_side = self.is_wall(Coordinates(x,y+1))
        except IndexError:
            return False

        if left_side and top_side:
            return True
        elif left_side and bottom_side:
            return True
        elif right_side and bottom_side:
            return True
        elif right_side and top_side:
            return True
        else:
            return False

    def check_stuck_boxes(self, boxes):
        for box in boxes:
            if box in self.stuck_points:
                return True
        return False