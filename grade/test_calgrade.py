from calgrade import calGrade
import unittest

class Test_Calculator(unittest.TestCase):
    def testSumFunction(self):
        self.assertEqual(calGrade(80),'A') 
        self.assertEqual(calGrade(70),'B') 
        self.assertEqual(calGrade(60),'C') 
        self.assertEqual(calGrade(50),'D') 
        self.assertEqual(calGrade(40),'F') 