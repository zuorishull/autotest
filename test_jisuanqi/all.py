import unittest
import time
import HTMLTestRunner

suite=unittest.TestSuite()
tests=unittest.defaultTestLoader.discover("../test_jisuanqi",pattern="test*.py")
suite.addTests(tests)
now=time.strftime("%Y%m%d %H%M%S",time.localtime())
reportFile="./"+now+"_result.html"
fp=open(reportFile,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'计算器')
runner.run(suite)
fp.close()
