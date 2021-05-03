import unittest
import q3

class TestCase(unittest.TestCase):
    def testVolume(self):
        self.assertEqual(q3.fullName("Peter", "LaMontagne"), "Peter LaMontagne")
        self.assertEqual(q3.fullName("Bruce$$$$", "Wayne"), "Bruce$$$$ Wayne")
        self.assertEqual(q3.fullName("Peter", "Ames", "LaMontagne"), "Peter Ames LaMontagne")


#enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)