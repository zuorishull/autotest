import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=None

class NativeApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 指定设备信息
        device = {}
        device['deviceName'] = '6DDIVWPJEE4P8PUW'
        device['platformName'] = 'Android'
        device['platformVersion'] = '13'
        device['automationName'] = 'UiAutomator2'
        device['appPackage'] = 'com.xunmeng.pinduoduo'
        device['appActivity'] = '.ui.activity.MainFrameActivity'
        device['noReset'] = True
        device['unicodeKeyboard'] = True
        device['resetKeyboard'] = True
        # 打开APP
        global driver
        driver = webdriver.Remote("127.0.0.1:4723/wd/hub", device)

    def testJinShop(self):
        global driver
        driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="搜索"]').click()
        driver.wait_activity(".activity.NewPageActivity",5)
        sleep(3)
        driver.find_element(By.CLASS_NAME,'//android.widget.EditText[@content-desc="搜索"]').send_keys("西湖阁老")
        driver.press_keycode(66)
        driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.view.ViewGroup/android.view.View').click()
        driver.find_element(By.XPATH, '//*[@text="全部商品"]').click()

    @classmethod
    def tearDownClass(cls):
        global driver
        driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)