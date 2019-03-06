class MoveRover:

    def __init__(self, rover, limits):
        self.rover = rover
        self.limits = limits

    def move(self):
        # import pdb; pdb.set_trace()
        coordinate = 'x' if self.rover.m in ('E', 'W') else 'y'
        if self.rover.m in ('N', 'E'):
            setattr(self.rover, coordinate, self.rover.dict()[coordinate] + 1)
        elif self.rover.m in ('S', 'W'):
            setattr(self.rover, coordinate, self.rover.dict()[coordinate] - 1)
        self.check_limits(coordinate)

        return self.rover

    def check_limits(self, coordinate):
        # Check if rover touched the upper or bottom line
        if self.rover.dict()[coordinate] > self.limits[coordinate]:
            setattr(self.rover, coordinate, self.limits[coordinate])
            self.rover.dict()[coordinate] = self.limits[coordinate]
        elif self.rover.dict()[coordinate] < 0:
            setattr(self.rover, coordinate, 0)
