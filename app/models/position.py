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