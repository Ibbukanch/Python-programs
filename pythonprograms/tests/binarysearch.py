from Bridgelabz.pythonprograms.Algorithm.binarysearch import binarysearch
import unittest
class BinarySearch(unittest.TestCase):
    # Test Cases
    def test_binarysearch(self):
        reusult =binarysearch(['My', 'Name', 'is', 'Ibrahim', 'what', 'yours'], 'IBRAHIM')
        expected = 1
        self.assertEqual(reusult, expected)


if __name__ == '__main__':
    unittest.main()