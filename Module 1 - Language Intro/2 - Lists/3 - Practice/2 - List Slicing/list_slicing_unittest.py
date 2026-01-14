import unittest
import list_slicing_pp as pp

class TestListSlicing(unittest.TestCase):
    def test_numbers(self):
        self.assertIsNotNone(pp.numbers, "Did you change numbers?")
        self.assertEqual(pp.numbers, [5, 10, 15, 20, 25, 30])

    def test_over_10(self):
        self.assertIsNotNone(pp.over_10, "Did you change over_10?")
        self.assertEqual(pp.over_10, [15, 20, 25, 30])

    def test_under_20(self):
        self.assertIsNotNone(pp.under_20, "Did you change under_20?")
        self.assertEqual(pp.under_20, [5, 10, 15])

    def test_median(self):
        self.assertIsNotNone(pp.median, "Did you change the median?")
        self.assertEqual(pp.median, [15, 20])


if __name__ == '__main__':
    unittest.main()