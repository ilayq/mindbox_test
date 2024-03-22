from unittest import TestCase
from math import pi

from figure_area import Circle, Triangle, Area 


class TestFigures(TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertEqual(pi * 5 ** 2, Area(circle).scalar())

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(3 * 4 / 2, Area(triangle).scalar())

