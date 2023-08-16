import unittest

from app import multi


class TestMulti(unittest.TestCase):

    def test_multi_function(self):
        self.assertEqual(multi(2, 3), 6)
        self.assertEqual(multi(4, 5), 20)

    def test_add_function_with_floats(self):
        self.assertAlmostEqual(multi(1.5, 2.6), 3.9)


if __name__ == "__main__":
    unittest.main()
