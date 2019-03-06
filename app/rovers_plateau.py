from app.models.position import Position
from app.services.move_rover import MoveRover


class RoversPlateau:

    def __init__(self, upper_right):
        self.upper_right = {'x': int(upper_right[0]),
                            'y': int(upper_right[1])}

    def move(self, position, instructions):
        position_list = position.split(' ')
        self.current_position = Position(position_list[0],
            position_list[1], position_list[2])
        move_rover = MoveRover(self.current_position, self.upper_right)
        instructions_list = list(instructions)

        for i in instructions_list:
            if i == 'M':
                move_rover.move()
            else:
                move_rover.turn()

    def get_current_position(self):
        return "%s %s %s" % (self.current_position.x,
                             self.current_position.y,
                             self.current_position.m)
