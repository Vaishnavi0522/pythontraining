import unittest
from validate import validateUP

class validtest(unittest.Testcase):
    def testval1(selfself):
       self.asserEqual(validateUP('Vaishnavi','v@ishu2205'),True)

    def testval2(selfself):
        self.asserEqual(validateUP(55, 'v@ishu2205'), False)

    def testval3(selfself):
        self.asserEqual(validateUP('Vai', 'vaishu2205'), False)

    def testval4(selfself):
        self.asserEqual(validateUP(0, 'V@ishu2205'), False)

    def testval5(selfself):
        self.asserEqual(validateUP('vaishnavi p', 'v@ishu2205'), False)

    def setUP(self):
        print("setup")

    def teardown(self):
        print ("teardown")
if __name__ == '__main__':
    unittest.main()