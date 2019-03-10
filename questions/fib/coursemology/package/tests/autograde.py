import unittest
# Needs xmlrunner: pip install unittest-xml-reporting
import xmlrunner
import sys

class PublicTestsGrader(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing metadata for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }
    def test_public_01(self):
        self.meta['expression'] = "fib(0)"
        self.meta['expected'] = str(0)
        
        _out = fib(0)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, 0)
    def test_public_02(self):
        self.meta['expression'] = "fib(1)"
        self.meta['expected'] = str(1)
        
        _out = fib(1)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, 1)
    def test_public_03(self):
        self.meta['expression'] = "fib(8)"
        self.meta['expected'] = str(21)
        
        _out = fib(8)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, 21)

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
