import unittest

class toTest(unittest.TestCase):
#test has to start with test_
    def test_x(self):
        x = 1
        self.assertEqual(x, 1)

if __name__ == '__main__':
    unittest.main()