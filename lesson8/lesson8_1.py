import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(5, add(2,3))

    def test_add_negative_numbers(self):
        self.assertEqual(-5, add(-2,-3))
