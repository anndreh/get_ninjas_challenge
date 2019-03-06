import unittest
from app.models.position import Position


class TestPosition(unittest.TestCase):
    def setUp(self):
        self.position = Position(x=1,y=2,m='N')

    def test_position_x_is_not_none(self):
        self.assertIsNotNone(self.position.x)

    def test_position_y_is_not_none(self):
        self.assertIsNotNone(self.position.y)

    def test_position_m_is_not_none(self):
        self.assertIsNotNone(self.position.m)
