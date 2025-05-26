import dataclasses

@dataclasses
class Point:
    """

    """
    x: int
    y: int


    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
