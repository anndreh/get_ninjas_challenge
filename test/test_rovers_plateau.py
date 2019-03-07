import unittest
from app.rovers_plateau import RoversPlateau


class TestRoversPlateau(unittest.TestCase):
    def setUp(self):
        self.upper_right = [5,5]
        rover_position = '1 2 N'
        rover_instructions = 'LMLMLMLMM'
        self.expected_output = '1 3 N'
        self.rover_plateau = RoversPlateau(self.upper_right)
        self.rover_plateau.move(rover_position, rover_instructions)

    def test_output_is_not_null(self):
        self.assertIsNone

    def test_output_is_like_expected(self):
        self.assertEqual(self.expected_output,
            self.rover_plateau.get_current_position())