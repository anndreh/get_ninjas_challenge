from app.models.position import Position


class RoversPlateau:
    MOVE_OPTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, upper_right):
        self.upper_right = {'x': int(upper_right[0]),
                            'y': int(upper_right[1])}
        self.current_position = {}

    def move(self, position, instructions):
        position_list = position.split(' ')
        self.current_position = Position(position_list[0],
            position_list[1], position_list[2]).dict()
        instructions_list = list(instructions)

        for i in instructions_list:
            if i not in ('M', 'L', 'R'):
                return 'Instruction not allowed'
            if i == 'M':
                if self.current_position['m'] in ('N', 'S'): # Y coordinate
                    if self.current_position['m'] == 'N':
                        self.current_position['y'] += 1
                    else:
                        self.current_position['y'] -= 1
                    self.current_position['y'] = (self.check_limits('y',
                        self.current_position['y']))
                elif self.current_position['m'] in ('E', 'W'):
                    if self.current_position['m'] == 'E':
                        self.current_position['x'] += 1
                    else:
                        self.current_position['x'] -= 1
                    self.current_position['x'] = (self.check_limits('x',
                        self.current_position['x']))
            else:
                pos = [i for i,x in enumerate(self.MOVE_OPTIONS)
                            if x == self.current_position['m']][0] # Gets current direction
                if i == 'L':
                    self.current_position['m'] = self.MOVE_OPTIONS[pos-1]
                elif i == 'R':
                    if self.current_position['m'] == 'W': # Reached the end of the list
                        self.current_position['m'] = self.MOVE_OPTIONS[0]
                    else:
                        self.current_position['m'] = self.MOVE_OPTIONS[pos+1]

    def get_current_position(self):
        return self.current_position

    def check_limits(self, coordinate, value):
        # Check if rover touched the upper or bottom line
        if value > self.upper_right[coordinate]:
            value = self.upper_right[coordinate]
        elif value < 0:
            value = 0;
        return value