import unittest
import while_loop_pp as pp

class TestWhileLoop(unittest.TestCase):
    def testb(self):
        self.assertNotEqual(pp.b, 5, "The value of b didn't change")
        self.assertEqual(pp.b, 40)

    def testx(self):
        self.assertNotEqual(pp.x, 0, "The condition does not allow x to increment")
        self.assertEqual(pp.x, 3)

    def testc(self):
        self.assertNotEqual(pp.c, 3, "The value of c didn't change")
        self.assertEqual(pp.c, 96)

    def testy(self):
        self.assertNotEqual(pp.y, 0, "The incrementer does not increment")
        self.assertEqual(pp.y, 5)

    def testz(self):
        self.assertNotEqual(pp.z, 0, "x does not increment - either due to the condition or "
                                  "due to the counter")
        self.assertEqual(pp.z, 6)


if __name__ == '__main__':
    unittest.main()
