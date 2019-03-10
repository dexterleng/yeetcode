import unittest
# Needs xmlrunner: pip install unittest-xml-reporting
import xmlrunner
import sys

class PublicTestsGrader(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing metadata for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }
    def test_public_01(self):
        self.meta['expression'] = "sorted_squares([-4,-1,0,3,10])"
        self.meta['expected'] = str([0,1,9,16,100])
        
        _out = sorted_squares([-4,-1,0,3,10])
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, [0,1,9,16,100])
    def test_public_02(self):
        self.meta['expression'] = "sorted_squares([-7,-3,2,3,11])"
        self.meta['expected'] = str([4,9,9,49,121])
        
        _out = sorted_squares([-7,-3,2,3,11])
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, [4,9,9,49,121])

class PrivateTestsGrader(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing metadata for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }

class EvaluationTestsGrader(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing metadata for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }


# Do not modify beyond this line
if __name__ == '__main__':
    unittest.main(
            testRunner=xmlrunner.XMLTestRunner(open('report.xml', 'wb'), outsuffix = ''),
            failfast=False,
            buffer=False,
            catchbreak=False)
