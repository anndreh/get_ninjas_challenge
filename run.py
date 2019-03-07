import sys
from app.rovers_plateau import RoversPlateau


def main():
    upper_right = input('Inform the limit upper right for the plateau: ')
    rover_plateau = RoversPlateau(upper_right.split(' '))
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
    main()
