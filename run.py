import argparse
from app.move_rover import MoveRover


def main(args):
    print('Now inform the rover position or press "q" to quit.')
    rover_position = ''
    while rover_position != 'q':
        rover_position = raw_input('Rover position: ')
        rover_instructions = raw_input('Rover instructions: ')
        print(MoveRover(rover_position, rover_instructions)
            .move().getNewPosition())

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Robot rovers movements')
    parse.add_argument('--upper_right',
                       nargs='+', help='Upper right plateau', required=True)
    args = parse.parse_args()
    main(args)
