from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        self.testCases = {1: {'nums': [10, 2], 'output': '210'},
                          2: {'nums': [3, 30, 34, 5, 9], 'output': '9534330'}}

    @timeout(0.5)    
    def test_Case1(self):
        try:
            case = self.testCases[1]
            res = self.obj.largestNumber(case['nums'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
    @timeout(0.5)    
    def test_Case2(self):
        try:
            case = self.testCases[2]
            res = self.obj.largestNumber(case['nums'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    unittest.main()