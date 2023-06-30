from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas
import unittest
import parameterized


driver=None
data=pandas.read_excel("D:\\test.xlsx",sheet_name=0,names=["s1","op","s2","yq"],dtype={'s1':str,'op':str,'s2':str,'yq':str},header=None)
data=data.values.tolist()

class NativeApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 指定设备信息
        device = {}
        device['deviceName'] = '6DDIVWPJEE4P8PUW'
        device['platformName'] = 'Android'
        device['platformVersion'] = '13'
        device['automationName'] = 'UiAutomator2'
        device['appPackage'] = 'com.miui.calculator'
        device['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity'
        device['noReset'] = True
        device['unicodeKeyboard'] = True
        device['resetKeyboard'] = True
        # 打开APP
        global driver
        driver = webdriver.Remote("127.0.0.1:4723/wd/hub", device)
        sleep(10)

    @parameterized.parameterized.expand(data)
    def testCal(self,a,op,b,yq):
        global driver
        # driver.find_element(By.ID, "com.android.browser:id/search_hint").click()
        # driver.find_element(By.ID, "com.android.browser:id/url").send_keys("我是大帅哥")
        # driver.press_keycode(66)
        # sleep(5)
        # driver.find_element(By.ID, "com.android.browser:id/url").click()
        # driver.find_element(By.ID, "com.android.browser:id/url").send_keys("我真的是大帅哥")
        # driver.press_keycode(66)
        # sleep(5)
        if op=='+':
            oper='add'
        elif op=='-':
            oper='sub'
        elif op=='*':
            oper='mul'
        else:
            oper='div'

        for i in a:
            driver.find_element(By.ID, "com.miui.calculator:id/digit_"+i).click()
        driver.find_element(By.ID, "com.miui.calculator:id/op_"+oper).click()
        for i in b:
            driver.find_element(By.ID, "com.miui.calculator:id/digit_" + i).click()
        driver.find_element(By.ID, "com.miui.calculator:id/btn_equal_s").click()
        res=driver.find_element(By.ID, 'com.miui.calculator:id/result').text
        sleep(3)
        assert res==yq

    @classmethod
    def tearDownClass(cls):
        global driver
        # 关闭APP
        driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)





# data=[
#     ['520','+','1314','= 1,834'],
#     ['1314','-','520','= 794'],
#     ['5','*','2','= 10']
#     ]
# data=[]
# file=open("D:\\test.txt","r")
# for x in file:
#     data.append(x.split())
#     file.close()
#
# for i in range(len(data)):
#     if data[i][1] == '+':
#         data[i][1] = 'add'
#     elif data[i][1] == '-':
#         data[i][1] = 'sub'
#     elif data[i][1] == '*':
#         data[i][1] = 'mul'
#     else:
#         data[i][1] = 'div'
#
# for i in data:
#     for j in range(0,len(i)-1):
#         x=i[j]
#         if j!=1:
#             for a in x:
#                 driver.find_element(By.ID, "com.miui.calculator:id/digit_"+a).click()
#         else:
#             driver.find_element(By.ID, "com.miui.calculator:id/op_"+i[1]).click()
#     driver.find_element(By.ID, "com.miui.calculator:id/btn_equal_s").click()
#     res=driver.find_element(By.ID, 'com.miui.calculator:id/result').text
#     sleep(3)
#     if res==i[3]:
#         print("测试通过！")
#     else:
#         print("测试失败！")
# # 关闭APP
# driver.quit()


'''
#操作元素
driver.find_element(By.ID,"com.miui.calculator:id/digit_5").click()
driver.find_element(By.ID,"com.miui.calculator:id/digit_2").click()
driver.find_element(By.ID,"com.miui.calculator:id/digit_0").click()
driver.find_element(By.ID,"com.miui.calculator:id/op_add").click()
driver.find_element(By.ID,"com.miui.calculator:id/digit_1").click()
driver.find_element(By.ID,"com.miui.calculator:id/digit_3").click()
driver.find_element(By.ID,"com.miui.calculator:id/digit_1").click()
driver.find_element(By.ID,"com.miui.calculator:id/digit_4").click()
driver.find_element(By.ID,"com.miui.calculator:id/btn_equal_s").click()
res=driver.find_element(By.ID,'com.miui.calculator:id/result').text
sleep(3)
if res == '= 1,834':
    print("测试通过！")
else:
    print("测试失败！")

content=driver.page_source
sleep(5)
assert "我是大帅哥" in content
self.assertIn("我是大帅哥",content)


sleep(3)

'''
