class Position:

    def __init__(self, x, y, m):
        self.x = int(x)
        self.y = int(y)
        self.m = m

    def dict(self):
        return {
            'x': self.x,
            'y': self.y,
            'm': self.m
        }

    def move_vertically(self, limits):
        if self.m == 'N':
            self.y += 1
        else:
            self.y -= 1
        self.y = self.check_limits('y', self.y, limits)

    def move_horizontally(self, limits):
        if self.m == 'E':
            self.x += 1
        else:
            self.x -= 1
        self.x = self.check_limits('x', self.x, limits)

    def check_limits(self, coordinate, value, limits):
        # Check if rover touched the upper or bottom line
        if value > limits[coordinate]:
            value = limits[coordinate]
        elif value < 0:
            value = 0;
        return value