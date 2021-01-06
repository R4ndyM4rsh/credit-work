import unittest
from A import A
from B import B
a = B(4)
b = B(5)
c = B(6)
class TestA(unittest.TestCase):
    def test_one(self):
        res = a.one()
        self.assertEqual(res, 4)

        res = b.one()
        self.assertEqual(res, 5)

        res = c.one()
        self.assertEqual(res, 6)

    def test_two(self):
        res = a.two()
        self.assertEqual(res, 8)

        res = b.two()
        self.assertEqual(res, 10)

        res = c.two()
        self.assertEqual(res, "b")