from Bridgelabz.pythonprograms.Algorithm.Anagram import Anagram
import unittest


class anagram(unittest.TestCase):
    # test cases
    def test_anagram(self):
        result = Anagram('earth','heart')
        expected = True
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()
