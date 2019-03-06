import sys
import argparse
from app.rovers_plateau import RoversPlateau


def main(upper_right):
    rover_plateau = RoversPlateau(upper_right)
    print('Inform the position and instructions to each rover or "q" to quit.')
    rover_position = ''
    rover_instructions = ''
    while True:
        rover_position = input('Rover position: ')
        rover_instructions = input('Rover instructions: ')
        if rover_position == 'q' or rover_instructions == 'q':
            sys.exit()
        rover_plateau.move(rover_position, rover_instructions)
        print(rover_plateau.get_current_position())

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Robot rovers movements')
    parse.add_argument('--upper_right',
                       nargs='+', help='Upper right plateau', required=True)
    args = parse.parse_args()
    main(args.upper_right)
