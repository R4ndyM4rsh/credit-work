import unittest
from A import A
a = A(4)
b = A(5)
c = A(6)
class TestA(unittest.TestCase):
    def test_one(self):
        res = a.one()
        self.assertEqual(res, 5)

        res = b.one()
        self.assertEqual(res, 6)

        res = c.one()
        self.assertEqual(res, 5)

    def test_two(self):
        res = a.two()
        self.assertEqual(res, 6)

        res = b.two()
        self.assertEqual(res, 7)

        res = c.two()
        self.assertEqual(res, 5)

    def test_three(self):
        res = a.three()
        self.assertEqual(res, 7)

        res = b.three()
        self.assertEqual(res, "a")

        res = c.three()
        self.assertEqual(res, 9)

    def test_four(self):
        res = a.four()
        self.assertEqual(res, 8)

        res = b.four()
        self.assertEqual(res, 9)

        res = c.four()
        self.assertEqual(res, "5")