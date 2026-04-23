import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
#Question: The code would not be correct simply because test one passed. It just happens to be that 2 squared and doubled is the same number regardless, but that doesn't mean the function will always perform correctly as seen in the second test

