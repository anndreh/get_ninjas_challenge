import unittest
from app.models.position import Position


class TestPosition(unittest.TestCase):
    def setUp(self):
        self.data = {
            'x': 1,
            'y': 2,
            'm': 'N'
        }
        self.position = Position(
                self.data['x'],
                self.data['y'],
                self.data['m']
            )

    def test_position_x_is_not_none(self):
        self.assertIsNotNone(self.position.x)

    def test_position_y_is_not_none(self):
        self.assertIsNotNone(self.position.y)

    def test_position_m_is_not_none(self):
        self.assertIsNotNone(self.position.m)
