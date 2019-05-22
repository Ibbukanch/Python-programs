from com.Bridgelabz.Algorithm.bubblesort import bubbleSort
import unittest


class bubblesort(unittest.TestCase):
    try:
        # test cases
        def test_bubblesort(self):
            result = (bubbleSort([12,5,45,78,1,0]))
            expected = [0,1,5,12,45,78]
            self.assertEqual(expected, result)
    except:
        print("Failed")


if __name__ == '__main__':
    unittest.main()
