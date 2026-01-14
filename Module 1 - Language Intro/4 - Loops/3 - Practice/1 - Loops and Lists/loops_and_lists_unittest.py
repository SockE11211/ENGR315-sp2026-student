import unittest
import week2_for_loop_answerkey as pp

class TestWhileLoop(unittest.TestCase):
    def test_increment(self):
        self.assertNotEqual(pp.increment, 0, "Your incrementer does not increase")
        self.assertEqual(pp.increment, 4)

    def test_total(self):
        self.assertNotEqual(pp.total, 0, "Your total doesn't add up")
        self.assertEqual(pp.total, 42)

if __name__ == '__main__':
    unittest.main()