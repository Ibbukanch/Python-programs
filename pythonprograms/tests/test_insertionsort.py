from com.Bridgelabz.Algorithm.Insertionsort import insertionSort
import unittest


class Insertionsort(unittest.TestCase):
    try:
        # test cases
        def test_insertionsortout(self):
            result = (insertionSort(['bc','aa','ab']))
            expected = ['aa','ab','bc']
            self.assertEqual(expected, result)
    except:
        print("Failed:")


if __name__ == '__main__':
    unittest.main()
