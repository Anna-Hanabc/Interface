
#coding=utf-8
import requests
import unittest
#导入当前工程，才可以找到UnitestCase包
import sys
import os 
#sys.path.append("C://Users/HAN/.vscode/Interface")
case_path = os.getcwd() + "/UnitestCase/"
print(case_path)

# from UnitestCase.test_case01 import TestCase01
# from UnitestCase.test_case02 import TestCase02
# from UnitestCase.test_case03 import TestCase03

# case01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)

# suote = unittest.TestSuite([case01,case02,case03])
# unittest.TextTestRunner().run(suote)

discover = unittest.defaultTestLoader.discover(case_path)
print(discover)
unittest.TextTestRunner().run(discover)