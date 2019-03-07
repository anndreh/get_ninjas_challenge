import unittest
from app.models.position import Position
from app.rovers_plateau import RoversPlateau
from app.services.move_rover import MoveRover


class TestMoveRover(unittest.TestCase):
    def setUp(self):
        self.upper_right = {'x': 5, 'y': 5}
        self.data_position = [1, 2, 'N']
        self.data_position_limits = [5, 5, 'E']
        self.data_instructions = {
            'move_foward': 'M',
            'turn_left': 'L',
            'turn_right': 'R'
        }
        self.expected_after_move = {
            'x': 1,
            'y': 3,
            'm': 'N'
        }
        self.expected_after_turn_left = {
            'x': 1,
            'y': 2,
            'm': 'W'
        }
        self.expected_after_turn_right = {
            'x': 1,
            'y': 2,
            'm': 'E'
        }
        self.expected_after_move_to_limit = {
            'x': 5,
            'y': 5,
            'm': 'E'
        }

    def test_rover_move_foward(self):
        self.position = Position(*self.data_position)
        self.move_rover = MoveRover(self.position, self.upper_right)
        self.move_rover.move()
        self.assertEqual(self.expected_after_move, self.position.dict())

    def test_rover_move_turn_left(self):
        self.position = Position(*self.data_position)
        self.move_rover = MoveRover(self.position, self.upper_right)
        self.move_rover.turn('L')
        self.assertEqual(self.expected_after_turn_left, self.position.dict())

    def test_rover_move_turn_right(self):
        self.position = Position(*self.data_position)
        self.move_rover = MoveRover(self.position, self.upper_right)
        self.move_rover.turn('R')
        self.assertEqual(self.expected_after_turn_right, self.position.dict())

    def test_rover_move_to_limit(self):
        self.position = Position(*self.data_position_limits)
        self.move_rover = MoveRover(self.position, self.upper_right)
        self.move_rover.move()
        self.assertEqual(self.expected_after_move_to_limit,
            self.position.dict())
