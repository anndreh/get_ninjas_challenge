from app.models.position import Position
from app.services.move_rover import MoveRover


class RoversPlateau:
    MOVE_OPTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, upper_right):
        self.upper_right = {'x': int(upper_right[0]),
                            'y': int(upper_right[1])}

    def move(self, position, instructions):
        position_list = position.split(' ')
        self.current_position = Position(position_list[0],
            position_list[1], position_list[2])
        instructions_list = list(instructions)

        for i in instructions_list:
            if i == 'M':
                self.current_position = MoveRover(self.current_position, self.upper_right).move()
            else:
                pos = [i for i,x in enumerate(self.MOVE_OPTIONS)
                       if x == self.current_position.m][0] # Gets current direction
                if i == 'L':
                    self.current_position.m = self.MOVE_OPTIONS[pos-1]
                elif i == 'R':
                    if self.current_position.m == 'W': # Reached the end of the list
                        self.current_position.m = self.MOVE_OPTIONS[0]
                    else:
                        self.current_position.m = self.MOVE_OPTIONS[pos+1]

    def get_current_position(self):
        return "%s %s %s" % (self.current_position.x,
                             self.current_position.y,
                             self.current_position.m)
