class MoveRover:
    MOVE_OPTIONS = ['N', 'E', 'S', 'W']

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

    def turn(self, direction):
        pos = [i for i,x in enumerate(self.MOVE_OPTIONS)
               if x == self.rover.m][0] # Gets current direction
        if direction == 'L':
            self.rover.m = self.MOVE_OPTIONS[pos-1]
        elif direction == 'R':
             # Reached the end of the list
            self.rover.m = (self.MOVE_OPTIONS[0] if self.rover.m == 'W'
                else self.MOVE_OPTIONS[pos+1])

    def check_limits(self, coordinate):
        # Check if rover touched the upper or bottom line
        if self.rover.dict()[coordinate] > self.limits[coordinate]:
            setattr(self.rover, coordinate, self.limits[coordinate])
            self.rover.dict()[coordinate] = self.limits[coordinate]
        elif self.rover.dict()[coordinate] < 0:
            setattr(self.rover, coordinate, 0)
