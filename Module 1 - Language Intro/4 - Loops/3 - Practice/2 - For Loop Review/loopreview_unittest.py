import unittest
import week2_loopsreview_answerkey as pp

class TestLoopsReview(unittest.TestCase):
    def test_violence(self):
        self.assertIsNotNone(pp.violence, "The variable violence wasn't changed")
        self.assertEqual(pp.violence, True, "The variable violence is false")

    def test_total_adds(self):
        self.assertIsNotNone(pp.total_adds, "Total was not changed")
        self.assertEqual(pp.total_adds, 12)

    def test_new_stuff(self):
        self.assertNotEqual(len(pp.new_stuff), True, "Did you change the list?")
        self.assertCountEqual(pp.new_stuff, [5, 7, 9])


if __name__ == '__main__':
    unittest.main()