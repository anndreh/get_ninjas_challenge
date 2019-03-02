class RoversPlateau():
    def __init__(self, upper_right):
        self.upper_right['x'] = upper_right[0]
        self.upper_right['y'] = upper_right[1]
        self.current_position = {}

    def move(self, position, instructions):
        position_list = position.split(' ')
        self.current_position = {'x': position_list[0],
                            'y': position_list[1],
                            'm': position_list[2]}
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
                elif self.current_position['m'] in ('E', 'W'):
                    if self.current_position['m'] == 'E':
                        self.current_position['x'] += 1
                    else:
                        self.current_position['x'] -= 1
                self.check_limits()
            else:
                self.current_position['m'] = i

    def check_limits(self): # Check if rover touched the upper or bottom line
        if self.current_position['y'] > self.upper_right['y']:
            self.current_position['y'] = self.upper_right['y']
        elif self.current_position['y'] < 0:
            self.current_position['y'] = 0;

        if self.current_position['x'] > self.upper_right['x']:
            self.current_position['x'] = self.upper_right['x']
        elif self.current_position['x'] < 0:
            self.current_position['x'] = 0