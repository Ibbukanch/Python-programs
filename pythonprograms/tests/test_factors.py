from Bridgelabz.pythonprograms.Functional.Factors import factors
import unittest


class MyTestCase(unittest.TestCase):
    # test cases
    def test_factors(self):
        result = (factors(60))
        expected = [2,2,3,5.0]
        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()
