import unittest
import q1

class TestCase(unittest.TestCase):
    def testVolume(self):
        self.assertEqual(q1.volume("one","two","three"), 6)
        self.assertEqual(q1.volume(-1, 0, 3), 0)
        self.assertEqual(q1.volume(1.5,1.5,1), 2.25)


#enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)