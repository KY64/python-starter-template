import unittest
from src.main import substract, add

class TestMain(unittest.TestCase):
    def test_add(self):
        result = add(9, 7)
        self.assertEqual(result, 16)

    def test_substract(self):
        result = substract(9, 7)
        self.assertEqual(result, 2)
