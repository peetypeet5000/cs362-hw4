import unittest
import q2

class TestCase(unittest.TestCase):
    def testVolume(self):
        self.assertEqual(q2.listAverage([1,2,3]), 2)
        self.assertEqual(q2.listAverage([]), 2)
        self.assertEqual(q2.listAverage([-1,-6,-3]), (10/3))


#enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)