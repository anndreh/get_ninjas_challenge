import argparse
from app.move_rover import RoversPlateau


def main(upper_right):
    RoversPlateau(upper_right)
    print('Now inform the rover position or press "q" to quit.')
    rover_position = ''
    while rover_position != 'q':
        rover_position = raw_input('Rover position: ')
        rover_instructions = raw_input('Rover instructions: ')
        RoversPlateau.move_rover(rover_position, rover_instructions)

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Robot rovers movements')
    parse.add_argument('--upper_right',
                       nargs='+', help='Upper right plateau', required=True)
    upper_right_arg = parse.parse_args()
    main(upper_right_arg)
